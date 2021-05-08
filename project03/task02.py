import math
from task01 import *


def init(G, s):
    """
        Funkcja nadająca wartości początkowe atrybutom
        d i p dla wierzchołków grafu G\n
        G - zbiór wierzchołków grafu\n
        s - numer startowego wierzchołka (numeracja od zera)\n
        d - wagi najkrótszych ścieżek od wierzchołka s do pozostałych\n
        p - lista poprzedników
    """
    d = []
    p = []
    for i in range(len(G)):
        d.append(math.inf)
        p.append(None)
    d[s] = 0
    return d, p


def relax(u, v, w, d, p):
    """
        Funkcja wykonująca relaksację krawędzi (u, v)\n
        u, v - wierzchołki połączone krawędzią (u, v)\n
        w - wagi w grafie
    """
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        p[v] = u


def find_min_index(l):
    """
        Funkcja znajduje indeks wartości minimalnej w liście,
        która może zawierać również wartości None. 
    """
    min_val = math.inf
    idx = 0
    for i in range(len(l)):
        if l[i] != None:
            if l[i] < min_val:
                min_val = l[i]
                idx = i
    return idx


def dijkstra(graph, s=1):
    """
        Algorytm Dijkstry\n
        graph - graf w postaci macierzy sąsiedztwa\n
        s - numer startowego wierzchołka (numeracja od jedynki,
        następnie funkcja zmienia numerację na od zera, dla
        uproszczenia indeksowania)
    """
    s = s-1
    if s >= len(graph) or s < 0:
        print("Podano niepoprawny numer wierzchołka")
        exit(-1)
    # w - wagi w grafie graph
    w = graph
    # G - zbiór wierzchołków grafu graph
    G = [i for i in range(len(graph))]
    (d, p) = init(graph, s)
    S = []
    while sorted(S) != G:
        # Wybór wierzchołka u o najmniejszym d(u) spośród niegotowych wierzchołków
        d_cpy = d.copy()
        u = find_min_index(d_cpy)
        while u in S:
            d_cpy[u] = None
            u = find_min_index(d_cpy)
        S.append(u)
        for v in G:
            if v != u and v not in S and w[u][v] != 0:
                relax(u, v, w, d, p)
    return d, p


def nmb_of_spaces(n):
    """
        Funkcja zwraca napis zawierający n spacji
    """
    s = ""
    for _ in range(n):
        s += " "
    return s


def find_single_path(p, v):
    """
        Funkcja znajduje ścieżkę od wierzchołka
        s (oznaczonego na liśce p przez None) do v
    """
    path = []
    prev = v
    while prev != None:
        path.append(prev+1)
        prev = p[prev]
    path.reverse()
    return path


def print_dijkstra(d, p):
    """
        Funkcja wypisująca odpowiednio sformatowane
        ścieżki od wierzchołka s do pozostałych
    """
    max_nmb_len_1 = len(str(len(d)))
    max_nmb_len_2 = len(str(max(d)))
    print("START: s =", p.index(None)+1)
    for i in range(len(d)):
        spaces_nmb_1 = max_nmb_len_1 - len(str(i+1))
        spaces_nmb_2 = max_nmb_len_2 - len(str(d[i]))
        print("d(", i+1, ")", nmb_of_spaces(spaces_nmb_1),
              " = ", d[i], nmb_of_spaces(spaces_nmb_2), " ==> [", sep='', end='')
        path = find_single_path(p, i)
        for j in range(len(path)-1):
            print(path[j], " - ", sep='', end='')
        print(path[len(path)-1], "]", sep='')


if __name__ == "__main__":
    #graph = generate_random_coherent_weighted_graph(12)
    graph = [
        [0, 8, 0, 9, 3, 9, 5],
        [8, 0, 0, 2, 4, 0, 1],
        [0, 0, 0, 0, 0, 4, 0],
        [9, 2, 0, 0, 0, 9, 0],
        [3, 4, 0, 0, 0, 4, 0],
        [9, 0, 4, 9, 4, 0, 0],
        [5, 1, 0, 0, 0, 0, 0]
    ]

    (d, p) = dijkstra(graph)
    print_dijkstra(d, p)
    draw_graph_from_adj_matrix(graph, 'test')
    pass
