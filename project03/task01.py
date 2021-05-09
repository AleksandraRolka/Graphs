from utils import *
import random as rnd


def set_random_weight(adj_matrix, a, b):
    '''
        W podanym grafie (macierzy sąsiedztwa) występujacym krawędziom
        przypisuje losowe wagi z podanego przedziału [a,b]
    '''
    for i in range(len(adj_matrix)):
        for j in range(i, len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                adj_matrix[i][j] = adj_matrix[j][i] = rnd.randint(a, b)    
    return adj_matrix


def generate_random_coherent_weighted_graph(n,a = 1,b = 10):
    '''
        Generuje losowy spójny graf prosty
        Dopóki nie zostanie spełniony warunek ciągu graficznego oraz by graf był spójny:
            - losuje randomowy ciąg graficzny o rozmiarze n (n-wierzchołków)
            - tworzy macierz sąsiedztwa na podstawie wygenerowanej sekwencji
        Mając do dyspozycji wygenerowany graf, istniejącym krawędzią 
        przypisuje losowe wagi z podanego przedziału [a,b] ( defaultowo [1,10] )
    '''
    seq = gen_random_seq(n)
    graph = seq_to_adj_matrix(seq) 
    graph = rearange_matrix_by_seq(graph, seq)
    while not only_one_comp(graph):
        seq = gen_random_seq(n)
        graph = seq_to_adj_matrix(seq)
        graph = rearange_matrix_by_seq(graph, seq)
    graph = set_random_weight(graph,a,b)
    return graph

if __name__ == "__main__":
    
    n = 8
    graph = generate_random_coherent_weighted_graph(n)
    print_matrix(graph)
    draw_graph_from_adj_matrix(graph,'graf1')
    
    