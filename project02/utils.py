from enum import Enum
import numpy as np
import random as rnd
import math
import matplotlib.pyplot as plt

import task01

PI = math.pi
# Funkcje z projektu pierwszego (modyfikacje w funkcjach draw_graph, print_graph, reprRecognizer) oraz dodatkowo:
# - funkcja readGraphFromFile

################################################################################################################################################
# Rozpoznawanie reprezentacji


class GraphRepr(Enum):
    """
        Typ wyliczeniowy służący do rozróżnienia
        poszczególnych reprezentacji
    """
    ADJ = 1
    INC = 2
    LIST = 3
    SEQ = 4
    OTHER = 5


def is_list(graph_repr):
    """
        Funkcja sprawdzająca czy reprezentacja jest listą sąsiedztwa
    """
    is_list = False
    rows = len(graph_repr)
    if rows > 0:
        cols = len(graph_repr[0])
        for i in range(rows):
            # Sprawdzenie czy długość wiersza jest zmienna
            if len(graph_repr[i]) != cols:
                is_list = True
            # Sprawdzenie czy występują wartości większe niż 1
            for j in graph_repr[i]:
                if j > 1:
                    is_list = True
                    break
            if is_list:
                break
        # Sprawdzanie czy jeśli v jest połączone z u, to u jest połączone z v
        # (pod warunkiem że u != v)
        if is_list:
            for i in range(rows):
                # Sprawdzanie czy dany wiersz nie zawiera duplikatów
                if len(graph_repr[i]) != len(set(graph_repr[i])):
                    is_list = False
                for j in range(len(graph_repr[i])):
                    el = graph_repr[i][j]
                    if el <= rows:
                        if i+1 not in graph_repr[el-1] or i+1 == el:
                            is_list = False
                    else:
                        is_list = False
                    if not is_list:
                        break
                if not is_list:
                    break
    return is_list


def is_adj(graph_repr):
    """
        Funkcja sprawdzająca czy reprezentacja jest macierzą sąsiedztwa
    """
    rows = len(graph_repr)
    if rows > 0:
        cols = len(graph_repr[0])
        # Sprawdzenie czy macierz jest kwadratowa
        if rows != cols:
            return False
        for i in range(rows):
            # Sprawdzenie czy na diagonali występują wartości niezerowe
            if graph_repr[i][i] != 0:
                return False
            for j in range(cols):
                # Sprawdzenie czy macierz jest symetryczna i składa się z wartości {0, 1}
                if graph_repr[i][j] != graph_repr[j][i] or graph_repr[i][j] not in [0, 1]:
                    return False
        return True
    return False


def is_inc(graph_repr):
    """
        Funkcja sprawdzająca czy reprezentacja jest macierzą
        incydencji
    """
    rows = len(graph_repr)
    if rows > 0:
        cols = len(graph_repr[0])
        for i in range(cols):
            # Sprawdzenie czy suma w kolumnie jest równa 2
            sum = 0
            for j in range(rows):
                sum += graph_repr[j][i]
                # Sprawdzenie czy macierz składa się z wartości {0, 1}
                if graph_repr[j][i] not in [0, 1]:
                    return False
            if sum != 2:
                return False
        return True
    return False


def repr_recognizer(graph):
    """
        Funkcja zwracająca rozpoznaną reprezentację grafu, w zależności
        od przekazanego argumentu
    """
    repr = None
    # Sprawdzamy czy graph jest typu numpy.ndarray
    if isinstance(graph, np.ndarray):
        graph = graph.tolist()
    # Sprawdzamy czy graph jest listą 2D
    if isinstance(graph[0], list):
        # Jeśli tylko jeden wiersz to mamy do czynienia z ciągiem graficznym
        if len(graph) == 1:
            graph = graph[0]
        else:
            if is_list(graph):
                repr = GraphRepr.LIST
            elif is_adj(graph):
                repr = GraphRepr.ADJ
            elif is_inc(graph):
                repr = GraphRepr.INC
            else:
                repr = GraphRepr.OTHER
    # Jeśli graph jest tablicą 1D int-ów to mamy do czynienia z ciągiem graficznym
    if isinstance(graph[0], int):
        repr = GraphRepr.SEQ if task01.degree_seq(
            graph, len(graph)) else GraphRepr.OTHER
    # Funkcja zwraca też listę graph, żeby ta była odpowiednio przekształcona w przypadku ciągu graficznego
    return (repr, graph) if repr else (GraphRepr.OTHER, graph)

################################################################################################################################################
# Operacje I/O


def print_graph(graph):
    """
        Funkcja wypisująca przekazaną reprezentację grafu na ekran
    """
    (repr, _) = repr_recognizer(graph)
    if repr in [GraphRepr.INC, GraphRepr.ADJ]:
        if repr == GraphRepr.ADJ:
            print("Macierz sąsiedztwa:")
        else:
            print("Macierz incydencji:")
        for row in graph:
            for el in row:
                print(el, end=' ')
            print()
    elif repr == GraphRepr.LIST:
        print("Lista sąsiedztwa:")
        i = 0
        for row in graph:
            i += 1
            print(i, ":", sep='', end=' ')
            for el in row:
                print(el, end=' ')
            print()
    elif repr == GraphRepr.SEQ:
        print("Ciąg graficzny:")
        print("(", end="")
        for i in range(len(graph)-1):
            print(graph[i], ",", sep="", end=" ")
        print(graph[len(graph)-1], ")", sep="")
    else:
        print("Niepoprawny zapis")


def read_graph_from_file(filename):
    """
        Funkcja wczytująca reprezentację grafu z podanego pliku i zwracająca ją w postaci listy
    """
    try:
        with open(filename, "r") as f:
            graph = [[el for el in line.split(' ')] for line in f]
        # Rozpoznawanie czy któraś z linii nie jest pusta
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == '\n':
                    graph[i].pop(j)
                else:
                    graph[i][j] = int(graph[i][j])
        if not graph:
            print("Podany plik jest pusty")
            exit()
    except FileNotFoundError:
        print("Podany plik nie istnieje")
        exit()
    except ValueError:
        print("Podany plik zawiera nieprawidłowe wartości")
        exit()
    return graph

################################################################################################################################################
# Zmiana reprezentacji


def inc2adj(inc_matrix):
    """
                Funkcja zamiany macierzy incydencji na macierz sąsiedztwa
                inc_matrix - macierz incydencji
    """
    rows = len(inc_matrix)
    columns = len(inc_matrix[0])
    adj_matrix = [[0 for i in range(0, rows)] for i in range(0, rows)]
    # szukamy w kolumnie inc_matrix jedynki i zapisujemy numery wierszy tych elementow w dim
    # nastepnie w adj_matrix elementy o indeksach z dim ustawiamy na 1
    for i in range(0, columns):
        dim = []
        for j in range(0, rows):
            if (inc_matrix[j][i]) == 1:
                dim.append(j)
        adj_matrix[dim[0]][dim[1]] = 1
        adj_matrix[dim[1]][dim[0]] = 1
    return adj_matrix


def list2adj(graph_list):
    """
        Funkcja zamiany listy sąsiedztwa na macierz sąsiedztwa
        graph_list - lista sąsiedztwa
    """
    size = len(graph_list)
    adj_from_list = [[0 for i in range(0, size)] for i in range(0, size)]
    # przechodzimy petla po liscie, tworzymy macierz sasiedztwa,
    # nadajemy wartosc 1 elementom macierzy sasiedztwa o indeksach rownych
    # numerowi wiersza listy oraz wartosci aktualnego elementu pomniejszonego o jeden (aby zachowac indeksowanie)
    for i in range(0, size):
        for el in graph_list[i]:
            adj_from_list[i][el-1] = 1
    return adj_from_list


def adj2inc(matrix):
    """
                Funkcja zamiany macierzy sąsiedztwa na macierz incydencji
                matrix - macierz sąsiedztwa
    """
    size = len(matrix)
    inc_matrix = [[] for i in range(0, size)]
    # przechodzimy petla po trojkacie macierzy sasiedztwa, jesli element macierzy
    # rowny jest 1, w macierzy incydencji dodajemy kolumne, gdzie
    # jedynkami sa elementy o numerze wiersza rownym indeksom macierzy sasiedztwa - i,j
    for i in range(0, size):
        for j in range(0, i + 1):
            if matrix[i][j] == 1:
                for k in range(0, size):
                    if k == i or k == j:
                        inc_matrix[k].append(1)
                    else:
                        inc_matrix[k].append(0)
    return inc_matrix


def list2inc(graph_list):
    """
                Funkcja zamiany listy na macierz incydencji
                graph_list - lista sąsiedztwa
    """
    size = len(graph_list)
    matrix_inc_from_list = [[] for i in range(0, size)]
    # przechodzimy petla po liscie
    for i in range(0, size):
        for el in graph_list[i]:
            # aby nie powtarzac kolumn w macierzy incydencji
            if (el-1) <= i:
                # dodajemy kolumne z zerami
                # jedynkami w kolumnie sa elementy o indeksie numeru aktualnego
                # wiersza (i) oraz wartosci elementu (el-1) listy
                for k in range(0, size):
                    if k == i or k == (el-1):
                        matrix_inc_from_list[k].append(1)
                    else:
                        matrix_inc_from_list[k].append(0)
    return matrix_inc_from_list


def adj2list(matrix):
    """
                Funkcja zamiany macierzy sąsiedztwa na listę sąsiedztwa
                matrix - macierz sąsiedztwa
    """
    list_matrix = []
    # przechodzimy petla po macierzy sasiedztwa
    for i in range(0, len(matrix)):
        # dla kazdego wiersza tworzymy liste w list_matrix
        list_matrix.append([])
        for j in range(0, len(matrix[i])):
            # jesli element macierzy sasiedztwa w wierszu jest rowny 1
            # dolaczamy do wiersza list_matrix wartosc (numer kolumny + 1) (+1 aby indeksowanie sie zgadzalo)
            if matrix[i][j] == 1:
                list_matrix[i].append(j+1)
    return list_matrix


def inc2list(inc_matrix):
    """
                Funkcja zamiany macierzy incydencji na listę sąsiedztwa
                inc_matrix - macierz incydencji
    """
    rows = len(inc_matrix)
    columns = len(inc_matrix[0])
    list_from_inc = [[] for i in range(0, rows)]
    # szukamy w kolumnie inc_matrix jedynek i zapisujemy ich numery wierszy w dim
    # nastepnie w elemencie listy o numerze indeksu zapisanym w dim zapisujemy drugi indeks powiekszony o jeden
    for i in range(0, columns):
        dim = []
        for j in range(0, rows):
            if (inc_matrix[j][i]) == 1:
                dim.append(j)
        list_from_inc[dim[0]].append(dim[1]+1)
        list_from_inc[dim[1]].append(dim[0]+1)
    return list_from_inc

################################################################################################################################################
# Rysowanie grafu


def draw_graph(nodes_num, edges, fname, colors=None):
    """
            Funkcja rysuje graf na podstawie dwóch argumentów:
            - ilości wierzchołków (etykietowanie 1:ilość wierzchołków)
            - listy par krawędzi (od którego, do którego wierzchołka)
    """
    
    fname = 'images/' + fname
    if colors == None:
        colors = '#b3ccff'
    
    
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
    if not isinstance(colors, list):
        for i in range(nodes_num):
            ax.add_patch(plt.Circle((positions[i+1][0], positions[i+1][1]), nodesize, color=colors, zorder=3))
    else:
        for i in range(nodes_num):
            ax.add_patch(plt.Circle((positions[i+1][0], positions[i+1][1]), nodesize, color=colors[i], zorder=3))
            
    for i in range(nodes_num):
        ax.annotate(i+1, xy=(positions[i+1][0], positions[i+1][1]), fontsize=(nodesize*20), fontweight='ultralight', ha="center", va="center")

    # przeskalowanie osi, by nie ucinało obrazu wierzchołków oraz zapis do pliku .png
    fig.set_size_inches(20, 20)
    plt.xlim([0, 36 + nodesize/2])
    plt.ylim([0, 36 + nodesize/2])
    fig.savefig(fname, bbox_inches='tight')


def draw_graph_from_adj_matrix(matrix, fname, colors=None):
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
    draw_graph(nodes_num, edges, fname, colors)


def draw_graph_from_adj_list(adjlist, fname, colors=None):
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
    draw_graph(nodes_num, edges, fname, colors)


def draw_graph_from_incid_matrix(matrix, fname, colors=None):
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
    draw_graph(nodes_num, edges, fname, colors)

################################################################################################################################################
# Grafy losowe


def random_with_edges(n, l):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierzy incydencji
        z n wierzchołkami i l kwarędziami.
    """

    if n <= 1:
        print("Podaj co najmniej 2 wierzchołki")
        return

    if l < 1:
        print("Podaj co najmniej 1 krawedz")
        return

    matrix = np.zeros((n, l), dtype=int)

    # Na początku tworzymy listę wszystkich możliwych połączeń między
    # wierzchołami: [(0,1), (0,2), ..., (0,n-1), (1, 2), ..., (n-2, n-1)]
    # (wierzchołki numerujemy od 0 do n-1).
    avaliable_edges = [(i, j) for i in range(0, n) for j in range(i + 1, n)]

    if l > len(avaliable_edges):
        print("Za dużo krawędzi")
        return

    # Dokonujemy przetasowania w liście możliwych połączeń.
    rnd.shuffle(avaliable_edges)

    # Przechddzimy po kolumnach (krawędziach) macierzy incydencji
    # i uzupełniamy kolejne połączenia
    for i in range(0, l):
        edge = avaliable_edges[i]
        matrix[edge[0], i] = 1
        matrix[edge[1], i] = 1

    return matrix


def random_with_probability(n, p):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierz incydencji,
        z n wierzchołkami i p prawdopodobienstwem, które określa ile jest szans
        na to że pomiędzy dwoma wierzchołkami istnieje krawędź.
    """

    if p > 1 or p < 0:
        print("Prawdopodieństwo nie mieści się w przedziale [0, 1].")
        return

    if n <= 1:
        print("Podaj co najmniej 2 wierzchołki")
        return

    matrix = np.zeros((n, n), dtype=int)

    # W algorytmie przechodzimy po górnej macierzy trójkątnej i losujemy
    # czy między wierzchołkami pojawia się krawędź.
    for i in range(0, n):
        for j in range(i + 1, n):
            if rnd.random() <= p:
                matrix[i][j] = matrix[j][i] = 1

    return matrix

################################################################################################################################################