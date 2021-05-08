from task02 import *


def get_distance_matrix(graph):
    """
        Funkcja zwracająca macierz odległości między wszystkimi parami
        wierzchołków grafu graph
    """
    dm = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(len(graph)):
        (d, p) = dijkstra(graph, i+1)
        for j in range(i+1, len(graph)):
            dm[i][j] = dm[j][i] = d[j]
    return dm


if __name__ == "__main__":
    #graph = generate_random_coherent_weighted_graph(5)
    graph = [
        [0, 8, 0, 9, 3, 9, 5],
        [8, 0, 0, 2, 4, 0, 1],
        [0, 0, 0, 0, 0, 4, 0],
        [9, 2, 0, 0, 0, 9, 0],
        [3, 4, 0, 0, 0, 4, 0],
        [9, 0, 4, 9, 4, 0, 0],
        [5, 1, 0, 0, 0, 0, 0]
    ]

    dm = get_distance_matrix(graph)
    print_matrix(dm)
    draw_graph_from_adj_matrix(graph, 'test')
