import math
import matplotlib.pyplot as plt

PI = math.pi


# ----------------------------------------------------------------------------------
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
    Sx, Sy = 18, 18
    # lista współrzędnych położenia wierzchołków
    positions = {}
    # promień pojedynczego koła reprezentującego wierzchołek
    nodesize = 1 / math.log(nodes_num, 10)

    if nodes_num > 0:
        for i in range(nodes_num):
            # wyliczenie współrzędnych położenia wierzcholków równomiernie na kole
            positions.update(
                {(i + 1): (Sx + r * math.cos(i * alpha - PI / 2), Sy + r * math.sin(i * alpha + PI / 2))})

    # utworzenie figury, zestawu 'wykresów'
    fig, ax = plt.subplots()
    plt.axis('off')
    # narysowanie koła na którym znajdą się wierzchołki grafu
    ax.add_patch(plt.Circle((Sx, Sy), r, color='#808080',
                 lw=0.1, ls='-', fill=False))

    # wyrysowanie krawędzi
    for i in range(len(edges)):
        v1, v2 = edges[i][0], edges[i][1]
        p1 = (positions[v1][0], positions[v2][0])
        p2 = (positions[v1][1], positions[v2][1])
        plt.plot(p1, p2, color='k', linewidth=0.5)

    # wyrysowanie wierzchołków i ich etykiet
    for i in range(nodes_num):
        ax.add_patch(plt.Circle(
            (positions[i+1][0], positions[i+1][1]), nodesize, color='#b3ccff', zorder=3))
        ax.annotate(i+1, xy=(positions[i+1][0], positions[i+1][1]), fontsize=(
            nodesize*20), fontweight='ultralight', ha="center", va="center")

    # przeskalowanie osi, by nie ucinało obrazu wierzchołków oraz zapis do pliku .png
    fig.set_size_inches(20, 20)
    plt.xlim([0, 36 + nodesize/2])
    plt.ylim([0, 36 + nodesize/2])
    fig.savefig(fname, bbox_inches='tight')


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
    draw_graph(nodes_num, edges, fname)


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
