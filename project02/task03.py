from utils import *


def get_random_color():
    """
        Funkcja zwracająca losowy napis reprezentujący kolor RGB
    """
    def r(): return rnd.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


def components_r(nr, v, graph, comp):
    """
        Funkcja rekurencyjna przeszukująca graf wgłąb w poszukiwaniu
        kolejnych spójnych składowych
        graph - macierz sąsiedztwa
    """
    neighbours = []
    for i in range(len(graph)):
        if graph[v][i] == 1:
            neighbours.append(i)
    for n in neighbours:
        if comp[n] == -1:
            comp[n] = nr
            components_r(nr, n, graph, comp)


def components(graph):
    """
        Funkcja zwracająca listę przyporządkującą każdy wierzchołek
        do właściwej spójnej składowej
        graph - macierz sąsiedztwa
    """
    nr = 0
    comp = [-1 for _ in range(len(graph))]
    for v in range(len(graph)):
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_r(nr, v, graph, comp)
    return comp


def print_components(graph):
    """
        Funkcja wypisująca na ekran spójne składowe oraz numer największej
        składowej
        graph - macierz sąsiedztwa
    """
    comp = components(graph)
    comps = [0 for _ in range(max(comp))]
    # Pętla licząca, ile wierzchołków należy do danej składowej
    for nmb in comp:
        comps[nmb-1] += 1
    # Pętla wypisująca na ekran kolejne składowe
    for c in range(len(comps)):
        print(c+1, ")", sep="", end=" ")
        for v in range(len(comp)):
            if comp[v] == c+1:
                print(v+1, end=" ")
        print()
    print("Największa składowa ma numer", comps.index(max(comps))+1)

    return comps.index(max(comps))+1, comps


def draw_components(graph, filename):
    """
        Funkcja rysująca graf w taki sposób, że każda spójna składowa
        ma inny kolor
        graph - macierz sąsiedztwa
    """
    comp = components(graph)
    colors_map = []
    colors = []
    # Pętla przydzielająca kolor każdej składowej
    for i in range(max(comp)):
        color = get_random_color()
        while color in colors:
            color = get_random_color()
        colors.append(color)
    # Pętla przydzielająca każdemu wierzchołkowi odpowiedni kolor
    # (wskazujący, do której składowej przynależy)
    for i in range(len(comp)):
        colors_map.append(colors[comp[i]-1])
    draw_graph_from_adj_matrix(graph, filename, colors_map)


if __name__ == "__main__":

    filename = "graph_representations/seq.txt"
    #graph = read_graph_from_file(filename)

    #graph = random_with_probability(10, 0.15)
    graph = random_with_edges(30, 20)

    (repr, graph) = repr_recognizer(graph)
    print_graph(graph)
    print()

    if repr == GraphRepr.INC:
        graph = inc2adj(graph)
    elif repr == GraphRepr.LIST:
        graph = list2adj(graph)
    elif repr == GraphRepr.SEQ:
        graph = seq_to_adj_matrix(graph)
    if repr != GraphRepr.OTHER:
        print_components(graph)
        draw_components(graph, "test")
