import random as rnd
from task01 import degree_seq, seq_to_adj_matrix
from utils_proj02 import *


def gen_random_seq_of_even_num(n):
    '''
        generuje ciąg losowych liczb parzystych
    '''
    deg = []
    seq = []
    k = int((n + 1) // 2) * 2

    for i in range(k):
        if i % 2 == 0:
            deg.append(i)

    e, d = 0, 0
    for i in range(n):
        if e < 3:
            while d == 0:
                d = rnd.choice(deg)
        else:
            d = rnd.choice(deg)
        e += 1
        seq.append(d)

    return seq



def gen_eulerian_seq(n):
    '''
        generuje losowy ciąg graficzny grafu Eulera
        ( - degree_seq - sprawdza czy ciąg jest graficzny )
        ( - gen_random_seq_of_even_num - generuje losowy ciąg parzystych liczb )
    '''
    seq = gen_random_seq_of_even_num(n)
    while not(degree_seq(seq, len(seq))):
        seq = gen_random_seq_of_even_num(n)
    # randomizacja kolejności stopni wierzchołków
    rnd.shuffle(seq)
    return seq



def only_one_comp(graph):
    '''
        sprawdza czy graf zawiera tylko jedną spójną składową 
        ( z pomięciem wierzchołków izolowanych )
    '''
    comps, max = components_list_and_max(graph)
    comps.remove(comps[max-1])
    for x in comps:
        if x > 1:
            return False
    return True




def find_eulerian_cycle(graph):
    '''
        zdajduje cykl Eulera w grafie Eulera
    '''
    # liczba wierzchołków
    n = len(graph)    
    # inicjalizacja pustego stosu oraz pustego cyklu
    stack = list() 
    cycle = list() 
    # początkowa wartość bieżącego wierzchołka jako indeksu pierwszego wierzchołka
    curr = 0
  
    # pętla iteruje dopóki stos nie jest pusty lub obecna krawędź ma sąsiada
    while(stack != [] or sum(graph[curr]) != 0): 
        # jeśli bieżący wierzchołek nie ma żadnego sąsiada
        # dodaje go do ścieżki, a ostatni element stosu ustawia jako bieżący, 
        # jednocześnie usuwając go ze stosu 
        if (sum(graph[curr]) == 0): 
            cycle.append(curr + 1) 
            curr = stack.pop(-1) 

        # jeśli bieżący wierzchołek ma co najmniej jeden sąsiedni wierzchołek
        # dodaje bieżący wierzchołek do stosu
        # usuwa krawędź między bieżącym a sąsiednim wierzchołkiem
        # ustawia bieżący wierzchołek (curr) na sąsiedni wierzchołek
        else: 
            for i in range(n): 
                if graph[curr][i] == 1: 
                    stack.append(curr) 
                    graph[curr][i] = 0
                    graph[i][curr] = 0
                    curr = i 
                    break
    
    # dodaje do cyklu ostatni bieżący wierzchołek (jest to pierwszy wierzchołek cyklu)
    cycle.append(curr + 1)
    
    return cycle

def gen_random_eulerian_graph_find_cycle(n):
    '''
        Funkcja generuje losowy graf Eulera o n wierzchołkach 
        i znajduje w nim ścieżkę Eulera
    '''
    seq = gen_eulerian_seq(n)
    graph = seq_to_adj_matrix(seq)  
    graph = rearange_matrix_by_seq(graph, seq)

    while not only_one_comp(graph):
        seq = gen_eulerian_seq(n)
        graph = seq_to_adj_matrix(seq)
        graph = rearange_matrix_by_seq(graph, seq)

    seq_subgraph = []
    csg_labels = []
    cycle = []

    for i in range(len(seq)):
        if seq[i] != 0:
            seq_subgraph.append(seq[i])
            csg_labels.append(i+1)

    # spójna część grafu 'graph' ( graf graph bez wierzchołków izolowanych )
    subgraph = matrix_remove_zeros(graph)
    cycle_list = find_eulerian_cycle(subgraph)
    
    for i in range(len(cycle_list)):

        cycle.append(csg_labels[cycle_list[i]-1])


    return seq, graph, cycle
