from random import randint, shuffle, choice
import numpy as np
from utils import *


def char_to_index(c):
    return ord(c) - ord('a') + 1


def random_network(n):

    layers = []

    # wartstwa 0 (źródło)
    layers.append(["S"])

    node_id = 'a'

    for i in range(n):

        layer = []
        nodes_in_layer = randint(2, n)

        for j in range(nodes_in_layer):
            layer.append(node_id)
            # dodajemy kolejny wierzchołek do wartswy
            node_id = chr(ord(node_id) + 1)

        layers.append(layer)

    # wartswa n+1 (ujście)
    layers.append(["T"])

    # zliczamy liczbe wszystkich wierzcholkow
    total_nodes = 0
    for layer in layers:
        total_nodes += len(layer)

    # tworzymy macierz sąsiedztwa
    adj_matrix = np.zeros((total_nodes, total_nodes), dtype='int')

    # łączenie warstw

    # krawędzie ze źródła
    for i in range(len(layers[1])):
        out_index = char_to_index(layers[1][i])
        adj_matrix[0][out_index] = randint(1, 10)

    # krawędzie w wartwach wewnętrznych
    for i in range(1, n):

        # pobieramy indeksy do macierzy sąsiedztwa z i-tej wartswy
        i_layer = layers[i]
        i_layer_indexes = []
        for node in i_layer:
            i_layer_indexes.append(char_to_index(node))

        # pobieramy indeksy do macierzy sąsiedztwa z i+1-szej wartswy
        inext_layer = layers[i + 1]
        inext_layer_indexes = []
        for node in inext_layer:
            inext_layer_indexes.append(char_to_index(node))

        # przypadek kiedy łączone wartswy są takiej samej wielkości
        if len(i_layer_indexes) == len(inext_layer_indexes):

            shuffle(i_layer_indexes)
            shuffle(inext_layer_indexes)

            for _ in range(len(i_layer_indexes)):
                in_index = i_layer_indexes.pop()
                out_index = inext_layer_indexes.pop()
                adj_matrix[in_index][out_index] = randint(1, 10)

        # przypadek kiedy warstwa i-ta jest większa
        elif len(i_layer_indexes) > len(inext_layer_indexes):

            next_layer_copy = inext_layer_indexes.copy()

            shuffle(i_layer_indexes)
            shuffle(inext_layer_indexes)
            shuffle(next_layer_copy)

            for _ in range(len(inext_layer_indexes)):
                in_index = i_layer_indexes.pop()
                out_index = inext_layer_indexes.pop()
                adj_matrix[in_index][out_index] = randint(1, 10)

            for _ in range(len(i_layer_indexes)):
                in_index = i_layer_indexes.pop()
                out_index = next_layer_copy.pop()
                adj_matrix[in_index][out_index] = randint(1, 10)

        # przypadek kiedy wartstwa i-ta jest mniejsza
        else:

            curr_layer_copy = i_layer_indexes.copy()

            shuffle(i_layer_indexes)
            shuffle(inext_layer_indexes)
            shuffle(curr_layer_copy)

            for _ in range(len(i_layer_indexes)):
                in_index = i_layer_indexes.pop()
                out_index = inext_layer_indexes.pop()
                adj_matrix[in_index][out_index] = randint(1, 10)

            for _ in range(len(inext_layer_indexes)):
                in_index = curr_layer_copy.pop()
                out_index = inext_layer_indexes.pop()
                adj_matrix[in_index][out_index] = randint(1, 10)

    # krawędzie do ujścia
    for i in range(len(layers[n])):
        in_index = char_to_index(layers[n][i])
        adj_matrix[in_index][total_nodes-1] = randint(1, 10)

    # dodajemy 2N łuków
    max_edges = 2 * n
    current_edges = 0

    while current_edges < max_edges:

        # losujemy wierzchołki
        u = randint(1, total_nodes-2)
        v = randint(1, total_nodes-2)

        if u != v and adj_matrix[u][v] == 0 and adj_matrix[v][u] == 0:
            adj_matrix[u][v] = randint(1, 10)
            current_edges += 1

    return adj_matrix, layers


if __name__ == "__main__":
    adj_matrix, layers = random_network(2)
    draw_graph_from_adj_matrix(adj_matrix, layers, with_weights=True)
