import math
import networkx as nx
import matplotlib.pyplot as plt

PI = math.pi



#----------------------------------------------------------------------------------

def draw_graph(nodes_num, edges, fname):
    """
        Funkcja rysuje graf na podstawie dwóch argumentów:
        - ilości wierzchołków (etykietowanie 1:ilość wierzchołków)
        - listy par krawędzi (od którego, do którego wierzchołka)
    """
    # wyliczenie kąta do równomiernego rozłożenia wierzchołków na okręgu
    alpha = (2 * PI) / nodes_num
    # promień okręgu
    r = 15
    # współrzędne środka okręgu
    Sx, Sy = 20, 20
    # lista współrzędnych położenia wierzchołków
    positions = {}

    # stworzenie pustego obiektu grafu, bez wierzchołków, bez krawędzi
    G = nx.Graph()
    if nodes_num > 0:
        # dodanie listy wierzchołków
        # domyślnie kolejne wierzchołki jako ich etykiety mają kolejne liczby naturalne
        G.add_nodes_from(list(range(1, nodes_num + 1)))
        # dodanie listy krawędzi
        G.add_edges_from(edges)

    for i in range(nodes_num):
        # wyliczenie współrzędnych położenia wierzcholków równomiernie na kole
        positions.update({(i + 1): (Sx + r * math.cos(i * alpha - PI / 2), Sy + r * math.sin(i * alpha + PI / 2))})


    # wyrysowanie wierzchołków, krawędzi grafu na kole i zapis do pliku .png
    fig = plt.figure()
    nx.draw(G, pos=positions, node_size=1200 * 20 / nodes_num, node_color='#b3ccff',
            font_size=(1200 * 20 / nodes_num) / 85, with_labels=True)
    plt.draw()
    fig.set_size_inches(12, 12)
    fig.savefig(fname)

# ----------------------------------------------------------------------------------

def draw_graph_from_adj_matrix(matrix, fname):
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
            if matrix[i][j] == 1:
                edges.append((i + 1, j + 1))

    # na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
    draw_graph(nodes_num, edges,fname)


def draw_graph_from_adj_list(adjlist, fname):
    """
        Funkcja rysuje graf na podstawie listy sąsiedztwa
        (wykorzystuje funkcję draw_graph)
    """

    # długość listy sąsiedztwa daje nam liczbę wierzchołków
    size1 = len(adjlist)
    nodes_num = size1
    edges = []

    # przechodzimy pętlami po liście sąsiedztwa
    for i in range(size1):
        for j in range(len(adjlist[i])):
            # zapisujemy informacje o występujących krawędziami (początek krawędzi w wierzchołku.., koniec w wierzchołku..)
            if adjlist[i][j]:
                edges.append((i + 1, adjlist[i][j]))

    # na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
    draw_graph(nodes_num, edges, fname)


def draw_graph_from_incid_matrix(matrix, fname):
    """
        Funkcja rysuje graf na podstawie macierzy incydencji
        (wykorzystuje funkcję draw_graph)
    """

    size1 = len(matrix)
    size2 = len(matrix[0])

    # pierwszy wymiar macierzy wskazuje liczbę wierzchołków
    nodes_num = size1
    edges = []

    # przechodzimy po wierszach i kolumnach podanej macierzy incydencji
    for j in range(size2):
        ends = []
        for i in range(size1):
            if matrix[i][j] == 1:
                ends.append(i + 1)
        edges.append((ends[0], ends[1]))

    # na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
    draw_graph(nodes_num, edges, fname)