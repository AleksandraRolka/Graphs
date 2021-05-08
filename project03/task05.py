from task01 import *
from utils import *
import numpy as np

def kruskal_algorhitm(graph):

    n = len(graph[0]) # get number of vertices
    edges_in_tree = n - 1

    minimal_spanning_tree = np.zeros((n, n), dtype=int)

    list_of_edges = []
    for i in range(n):
        for j in range(i, n):
            if graph[i][j] > 0:
                list_of_edges.append({"weight": graph[i][j], "indexes": [i, j]})


    list_of_edges.sort(key = lambda x : x["weight"])
    print("po sortowaniu")

    placed_edges = 0
    for edge in list_of_edges:

        # get index of vertices
        i = edge["indexes"][0]
        j = edge["indexes"][1]

        if not check_for_cycle(minimal_spanning_tree, i, j): # tu sprawdzamy czy dołożenie krawędzi spowoduje powstanie cyklu
            minimal_spanning_tree[i][j] = minimal_spanning_tree[j][i] = edge["weight"]
            placed_edges += 1

        if placed_edges >= edges_in_tree:
            break

    return minimal_spanning_tree

def check_for_cycle(graph, i, j):
    """
    Funkcja sprawdza czy w grafie podanym jako macierz sąsiedztwa
    dodanie krawędzi pomiędzy a i b spowoduje powstanie cyklu.
    """

    visited = np.zeros(len(graph[0]), dtype=bool)
    return dfs_search(graph, i, j, visited)


def dfs_search(graph, u, x, visited):
    """
    Funkcja przeszukująca graf w głąb poszukiwaniu wierzchołka x
    """

    visited[u] = True
    u_neighbours = [ i for i, e in enumerate(graph[u]) if e > 0 and not visited[i] ]

    for v in u_neighbours:
        if v == x:
            return True
        visited[v] = True
        if dfs_search(graph, v, x, visited):
            return True

    return False


if __name__ == "__main__":
    g = generate_random_coherent_weighted_graph(200, 1, 20)

    # draw_graph_from_adj_matrix(g, 'oryginalny')
    g2 = kruskal_algorhitm(g)
    # draw_graph_from_adj_matrix(g2, 'drzewo_rozpinajace')
