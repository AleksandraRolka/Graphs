from task03 import *


def find_graph_centers(graph):
    """
        Funkcja wyznacza centrum grafu graph
    """
    dm = get_distance_matrix(graph)
    # Sumy odległości dla poszczególnych wierzchołków
    dist_sum = []
    # Odległość od najdalszego wierzchołka
    dist_from_farthest = []
    for row in dm:
        dist_sum.append(sum(row))
        dist_from_farthest.append(max(row))
    return (dist_sum.index(min(dist_sum)), min(dist_sum), dist_from_farthest.index(min(dist_from_farthest)), min(dist_from_farthest))


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

    (center_idx, center_val, minimax_center_idx,
     minimax_center_val) = find_graph_centers(graph)
    print("Centrum = ", center_idx+1,
          " (suma odległości: ", center_val, ")", sep='')
    print("Centrum minimax = ", minimax_center_idx+1,
          " (odległość od najdalszego: ", minimax_center_val, ")", sep='')

    draw_graph_from_adj_matrix(graph, 'test')
