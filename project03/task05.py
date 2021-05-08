from task01 import *
from utils import *
import numpy as np

def union(a, b, sets):
    sets[a] = b

def find_set(v, sets):
    if sets[v] == v:
        return v
    return find_set(sets[v], sets)

def kruskal_algorithm(graph):

    n = len(graph[0]) # liczba wierzcholkow w grafie
    edges_in_tree = n - 1

    # tworzymy macierz sąsiedztwa która bedzie przechowywała MDR
    minimal_spanning_tree = np.zeros((n, n), dtype=int)

    list_of_edges = []
    for i in range(n):
        for j in range(i, n):
            if graph[i][j] > 0:
                list_of_edges.append({"weight": graph[i][j], "index": [i, j]})

    sets = []

    for i in range(n):
        sets.append(i)

    list_of_edges.sort(key = lambda x : x["weight"])

    placed_edges = 0
    for edge in list_of_edges:

        # get index of vertices
        i = edge["index"][0]
        j = edge["index"][1]

        i_set = find_set(i, sets)
        j_set = find_set(j, sets)

        if i_set != j_set:
            minimal_spanning_tree[i][j] = minimal_spanning_tree[j][i] = edge["weight"]
            union(i_set, j_set, sets)
            placed_edges += 1

        if placed_edges >= edges_in_tree:
            break

    return minimal_spanning_tree


if __name__ == "__main__":
    g = generate_random_coherent_weighted_graph(6)
    mst = kruskal_algorithm(g)
    draw_graph_with_mst(g, mst, 'drzewo_rozpinajace')
