import math
import matplotlib.pyplot as plt
import networkx as nx
import random as rnd
import math

PI = math.pi

# Funkcje z poprzednich projektów
################################################################################################################################################


def print_matrix(matrix):
    '''
            Wypisuje macierz w formie:\n
                0  1  1\n
                1  0  1\n
                1  1  0         
    '''
    for row in matrix:
        for el in row:
            print('%4d' % el, end='')
        print()


def draw_graph(nodes_num, layers, edges, flow=None, fname="test", colors=None, with_weights=False):
    """
            Funkcja rysuje graf na podstawie trzech argumentów:
            - ilości wierzchołków (etykietowanie 1:ilość wierzchołków)
            - listy par krawędzi (od którego, do którego wierzchołka)
            - listy kolorów, na jakie zostaną pokolorowane kolejne spójne składowe
    """
    fname = 'images/' + fname
    if colors == None:
        colors = '#b3ccff'

    # Kolorowanie krawędzi na czerwono oraz ich pogrubianie, jeśli przepływ jest niezerowy
    edges_colors = []
    edges_widths = []
    if flow != None:
        for k in range(len(edges)):
            i = edges[k][0] - 1
            j = edges[k][1] - 1
            if flow[(i, j)] != 0:
                edges_colors.append('red')
                edges_widths.append(2)
            else:
                edges_colors.append('black')
                edges_widths.append(1)
    else:
        edges_colors.append('black')
        edges_widths.append(1)

    # wyliczenie kąta do równomiernego rozłożenia wierzchołków na okręgu
    alpha = (2 * PI) / nodes_num
    # promień okręgu
    r = 15
    # współrzędne środka okręgu
    Sx, Sy = 20, 20
    # lista współrzędnych położenia wierzchołków
    positions = {}
    nodesize = 1500 / math.log(nodes_num, 10)

    wierzcholki = []
    for l in layers:
        for v in l:
            wierzcholki.append(v)

    # stworzenie pustego obiektu grafu, bez wierzchołków, bez krawędzi
    G = nx.MultiDiGraph()
    if nodes_num > 0:
        # dodanie listy wierzchołków
        # domyślnie kolejne wierzchołki jako ich etykiety mają kolejne liczby naturalne
        G.add_nodes_from(list(range(1, nodes_num + 1)))
        # dodanie listy krawędzi
        loop_edges = []
        for i in range(len(edges)):
            if edges[i][0] == edges[i][1]:
                loop_edges.append(edges[i])
            else:
                G.add_edge(edges[i][0], edges[i][1], weight=edges[i][2])

    labelsdicts = {}

    j = 0
    for i in range(len(layers)):
        for v in range(len(layers[i])):
            j += 1
            positions.update({(j): (100 + i * 50, 100 + v * 50)})
            labelsdicts[j] = wierzcholki[j-1]
        # positions.update({(i + 1): (20 * i, 100)})

    options = {
        'arrowstyle': '-|>',
        'arrowsize': 18,
    }

    # wyrysowanie wierzchołków, krawędzi grafu na kole i zapis do pliku .png
    fig = plt.figure()
    nx.draw(G, arrows=True, **options, pos=positions, node_size=nodesize, node_color=colors,
            font_size=nodesize / 85, labels=labelsdicts, with_labels=True,  edge_color=edges_colors, width=edges_widths)

    for i in range(len(loop_edges)):
        G.add_edge(loop_edges[i][0], loop_edges[i][1], weight=loop_edges[i][2])
    nx.draw_networkx_edges(
        G, pos=positions, edgelist=loop_edges, arrowstyle="<|-", style="curved")

    if with_weights:
        l = nx.get_edge_attributes(G, 'weight')
        labels = {}
        for key, value in l.items():
            if flow != None:
                labels[(key[0], key[1])] = str(
                    flow[(key[0]-1, key[1]-1)]) + "/" + str(value)
            else:
                labels[(key[0], key[1])] = value
        nx.draw_networkx_edge_labels(
            G, positions, edge_labels=labels, font_size=15, label_pos=0.35)

    plt.draw()
    fig.set_size_inches(12, 12)
    fig.savefig(fname)


def edges_from_adj_matrix(matrix):
    edges = []
    # przechodzimy pętlami po podanej macierzy sąsiedztwa
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami
            if matrix[i][j] != 0:
                edges.append((i+1, j+1, matrix[i][j]))
    return edges


def edges_from_adj_matrix_nodes_indexed_from_zero(matrix):
    edges = []
    # przechodzimy pętlami po podanej macierzy sąsiedztwa
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami ideksująć wierzchołki od zera
            if matrix[i][j] != 0:
                edges.append((i, j, matrix[i][j]))
    return edges


def draw_graph_from_adj_matrix(matrix, layers, flow=None, fname="test", colors=None, with_weights=False):
    """
            Funkcja rysuje graf na podstawie macierzy sąsiedztwa 
            (wykorzystuje funkcję draw_graph)
    """
    # pierwszy wymiar macierzy daje nam liczbę wierzchołków
    nodes_num = len(matrix)
    edges = edges_from_adj_matrix(matrix)

    # na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
    draw_graph(nodes_num, layers, edges, flow, fname, colors, with_weights)
