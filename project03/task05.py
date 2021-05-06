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
    
    placed_edges = 0
    for edge in list_of_edges:
        if True: # tu sprawdzamy czy dołożenie krawędzi spowoduje powstanie cyklu
            i = edge["indexes"][0]
            j = edge["indexes"][1]
            minimal_spanning_tree[i][j] = minimal_spanning_tree[j][i] = edge["weight"]
            placed_edges += 1
        if placed_edges >= edges_in_tree:
            break

    return minimal_spanning_tree

if __name__ == "__main__":
    g = generate_random_coherent_weighted_graph(8, 1, 10)

    g2 = kruskal_algorhitm(g)

    print_matrix(g2)
    draw_graph_from_adj_matrix(g2, 'graf2')