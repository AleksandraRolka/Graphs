from enum import Enum
import numpy as np
import random as rnd
import math
import copy
import matplotlib.pyplot as plt
import networkx as nx



PI = math.pi

# Funkcje z poprzednich projektów 

################################################################################################################################################

def gen_random_seq(n):

    seq = []

    for i in range(n):
        seq.append(rnd.randint(0, n))

    while not(degree_seq(seq, len(seq))):
        seq = gen_random_seq(n)
        
    return seq


def degree_seq(A, n):
    """
        Funkcja sprawdza czy dany ciag liczb jest ciagiem graficznym
        A - ciag liczb naturalnych
        n - liczba elementow w ciagu liczb
    """
    # sortujemy ciag nierosnaco
    A_s = sorted(A, reverse=True)
    # jesli ilosc nieparzystych elementow ciagu jest nieparzysta ciag nie jest graficzny
    if (sum(i % 2 for i in A_s)) % 2:
        return False
    while True:
        if all(el == 0 for el in A_s):
            return True
        elif A_s[0] < 0 or A_s[0] >= n or all(el < 0 for el in A_s[1:]):
            return False
        else:
            for i in range(1, A_s[0] + 1):
                if A_s[i] >= 1:
                    A_s[i] = A_s[i] - 1
                else:
                    return False
            A_s[0] = 0
            A_s.sort(reverse=True)

# ----------------------------------------------------------------------------------


def seq_to_adj_matrix(seq):
    """
        Funkcja tworzy macierz sasiedztwa na podstawie ciagu liczb
        seq - ciag liczb naturalnych

    """
    if degree_seq(seq, len(seq)) == False:
        print("Dana sekwencja liczb nie jest ciagiem graficznym!")
        return
    size = len(seq)
    seqSorted = copy.copy(seq)
    seqSorted.sort(reverse=True)

    # tworzymy liste par [numer wierzchołka-stopien]
    my_list = [[i, seqSorted[i]] for i in range(0, size)]
    # tworzymy zerowa macierz sasiadujaca nxn
    adj_matrix = [[0 for i in range(size)] for j in range(size)]

    for i in range(0, size):
        # sortujemy liste po stopniu
        my_list = sorted(my_list, key=lambda x: x[1], reverse=True)
        # od następnych par aktualego elementu listy odejmujemy 1 - tworzymy krawedz
        # oraz uaktualniamy macierz sasiedztwa
        for el in my_list[1: my_list[0][1]+1]:
            adj_matrix[my_list[0][0]][el[0]] = 1
            adj_matrix[el[0]][my_list[0][0]] = 1
            el[1] -= 1
        # aktualny element ma teraz odpowiednia liczbe krawedzi wychodzacych z niego - usuwamy go z listy
        my_list.pop(0)
        # sortujemy na nowo uaktualniona liste
        my_list = sorted(my_list, key=lambda x: x[1], reverse=True)

    return adj_matrix
    


def swap_rows(matrix, i, j):
    '''
        zamienia w macierzy wiersze i z j
    '''
    temp = matrix[i][:]
    matrix[i][:] = matrix[j][:]
    matrix[j][:] = temp
    return matrix

def swap_columns(matrix, i, j):
    '''
        zamienia w macierzy kolumny i z j
    '''
    for l in matrix:
        l[i], l[j] = l[j], l[i]
    return matrix
    
def rearange_matrix_by_seq(matrix, seq):
    '''
        dostosowywuje kolejności wierszy, kolumn grafu 
        do kolejności stopni wierzchołków podanego ciągu
    '''
    
    for i in range(len(seq)):
        for j in range(len(seq)):
            if sum(matrix[i]) == seq[i]:
                pass
            else:
                for s in range(i+1, len(matrix)):
                    if sum(matrix[s]) == seq[i]:
                        swap_rows(matrix, i, s)
                        swap_columns(matrix, i, s)

    return matrix

def print_matrix(matrix):
    '''
        wypisuje maciersz w formie:
        np. 0  1  1
            1  0  1
            1  1  0         
    '''
    for row in matrix:
        for el in row:
            print('%4d' % el,end='')
        print() 



def components_r(nr, v, graph, comp):
    """
        Funkcja rekurencyjna przeszukująca graf wgłąb w poszukiwaniu
        kolejnych spójnych składowych
        graph - macierz sąsiedztwa
    """
    neighbours = []
    for i in range(len(graph)):
        if graph[v][i] == 1:
            neighbours.append(i)
    for n in neighbours:
        if comp[n] == -1:
            comp[n] = nr
            components_r(nr, n, graph, comp)
            
def components(graph):
    """
        Funkcja zwracająca listę przyporządkującą każdy wierzchołek
        do właściwej spójnej składowej
        graph - macierz sąsiedztwa
    """
    nr = 0
    comp = [-1 for _ in range(len(graph))]
    for v in range(len(graph)):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, graph, comp)
    return comp

def only_one_comp(graph):
    '''
        sprawdza czy graf zawiera tylko jedną spójną składową 
    '''
    for i in range(len(components(graph))):
        if components(graph)[i] != 1:
           return False
    return True
	
################################################################################################################################################

def draw_graph(nodes_num, edges, fname, colors = None):
    """
        Funkcja rysuje graf na podstawie trzech argumentów:
        - ilości wierzchołków (etykietowanie 1:ilość wierzchołków)
        - listy par krawędzi (od którego, do którego wierzchołka)
        - listy kolorów, na jakie zostaną pokolorowane kolejne spójne składowe
    """
    fname = 'images/' + fname
    if colors == None:
        colors = '#b3ccff'
    # wyliczenie kąta do równomiernego rozłożenia wierzchołków na okręgu
    alpha = (2 * PI) / nodes_num
    # promień okręgu
    r = 15
    # współrzędne środka okręgu
    Sx, Sy = 20, 20
    # lista współrzędnych położenia wierzchołków
    positions = {}
    nodesize = 1500 / math.log(nodes_num, 10)
    
    # stworzenie pustego obiektu grafu, bez wierzchołków, bez krawędzi
    G = nx.Graph()
    if nodes_num > 0:
        # dodanie listy wierzchołków
        # domyślnie kolejne wierzchołki jako ich etykiety mają kolejne liczby naturalne
        G.add_nodes_from(list(range(1, nodes_num + 1)))
        # dodanie listy krawędzi
        for i in range(len(edges)):
            G.add_edge(edges[i][0],edges[i][1], weight=edges[i][2])

    for i in range(nodes_num):
        # wyliczenie współrzędnych położenia wierzcholków równomiernie na kole
        positions.update({(i + 1): (Sx + r * math.cos(i * alpha - PI / 2), Sy + r * math.sin(i * alpha + PI / 2))})

    # positions = nx.spring_layout(G)

    # wyrysowanie wierzchołków, krawędzi grafu na kole i zapis do pliku .png
    fig = plt.figure()
    nx.draw(G, pos=positions, node_size=nodesize, node_color=colors,
            font_size= nodesize / 85, with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=labels, font_size=15, label_pos=0.6)
    
    plt.draw()
    fig.set_size_inches(12, 12)
    fig.savefig(fname)



def draw_graph_from_adj_matrix(matrix, fname, colors = None):
    """
        Funkcja rysuje graf na podstawie macierzy sąsiedztwa 
        (wykorzystuje funkcję draw_graph)
    """
    size1 = len(matrix)
    size2 = len(matrix[0])

    # pierwszy wymiar macierzy daje nam liczbę wierzchołków
    nodes_num = size1
    edges = []

    # przechodzimy pętlami po podanej macierzy sąsiedztwa
    for i in range(size1):
        for j in range(size2):
            # zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami
            if matrix[i][j] != 0:
                edges.append((i + 1, j + 1,matrix[i][j]))


    # na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
    draw_graph(nodes_num, edges, fname, colors)


def draw_graph_with_mst(g, mst, fname, colors = None):
    """
        Funkcja rysuje graf na podstawie macierzy sąsiedztwa 
        (wykorzystuje funkcję draw_graph)
    """
    size1 = len(g)
    size2 = len(g[0])

    # pierwszy wymiar macierzy daje nam liczbę wierzchołków
    nodes_num = size1
    edges = []
    mst_edges = []

    # przechodzimy pętlami po podanej macierzy sąsiedztwa
    for i in range(size1):
        for j in range(size2):
            # zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami
            if g[i][j] > 0:
                edges.append((i + 1, j + 1, g[i][j]))

    # przechodzimy pętlami po podanej macierzy sąsiedztwa
    for i in range(size1):
        for j in range(i, size2):
            # zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami
            if mst[i][j] != 0:
                mst_edges.append((i + 1, j + 1, mst[i][j]))

    # na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
    fname = 'images/' + fname
    if colors == None:
        colors = '#b3ccff'
    # wyliczenie kąta do równomiernego rozłożenia wierzchołków na okręgu
    alpha = (2 * PI) / nodes_num
    # promień okręgu
    r = 15
    # współrzędne środka okręgu
    Sx, Sy = 20, 20
    # lista współrzędnych położenia wierzchołków
    positions = {}
    nodesize = 1500 / math.log(nodes_num, 10)

    # stworzenie pustego obiektu grafu, bez wierzchołków, bez krawędzi
    G = nx.Graph()
    if nodes_num > 0:
        # dodanie listy wierzchołków
        # domyślnie kolejne wierzchołki jako ich etykiety mają kolejne liczby naturalne
        G.add_nodes_from(list(range(1, nodes_num + 1)))
        # dodanie listy krawędzi
        for i in range(len(edges)):
            G.add_edge(edges[i][0],edges[i][1], weight=edges[i][2], width=2, color='black', fontsize=12)

        for i in range(len(mst_edges)):
            G.add_edge(mst_edges[i][0], mst_edges[i][1], weight=mst_edges[i][2], width=8, color='r', fontsize=20)

    for i in range(nodes_num):
        # wyliczenie współrzędnych położenia wierzcholków równomiernie na kole
        positions.update({(i + 1): (Sx + r * math.cos(i * alpha - PI / 2), Sy + r * math.sin(i * alpha + PI / 2))})

    # wyrysowanie wierzchołków, krawędzi grafu na kole i zapis do pliku .png
    widths = list(nx.get_edge_attributes(G, 'width').values())
    edge_colors = list(nx.get_edge_attributes(G, 'color').values())

    # positions = nx.spring_layout(G)

    fig = plt.figure()
    nx.draw(G, pos=positions, node_size=nodesize, node_color=colors,
            font_size= nodesize / 85, with_labels=True, width=widths, edge_color=edge_colors)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=labels, font_size=15, label_pos=0.6)
    
    plt.draw()
    fig.set_size_inches(12, 12)
    fig.savefig(fname)
