from task01 import *
from utils import *
import numpy as np

def union(a, b, subsets):
    subsets[a] = b

def find_set(v, subsets):
    if subsets[v] == v:
        return v
    return find_set(subsets[v], subsets)

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

    subsets = []

    for i in range(n):
        subsets.append(i)

    list_of_edges.sort(key = lambda x : x["weight"])

    placed_edges = 0
    sum_of_weights = 0

    for edge in list_of_edges:

        # get index of vertices
        i = edge["index"][0]
        j = edge["index"][1]

        i_set = find_set(i, subsets)
        j_set = find_set(j, subsets)

        if i_set != j_set:
            minimal_spanning_tree[i][j] = minimal_spanning_tree[j][i] = edge["weight"]
            union(i_set, j_set, subsets)
            sum_of_weights += edge["weight"]
            placed_edges += 1

        if placed_edges >= edges_in_tree:
            break

    return minimal_spanning_tree, sum_of_weights


if __name__ == "__main__":
    g = generate_random_coherent_weighted_graph(6)
    mst, cost = kruskal_algorithm(g)
    draw_graph_with_mst(g, mst, 'drzewo_rozpinajace')
