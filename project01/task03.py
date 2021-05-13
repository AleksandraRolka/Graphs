import random as rnd


def random_with_edges(n, l):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierzy incydencji
        z n wierzchołkami i l krawędziami.
    """

    if n <= 1:
        print("-gnl: podaj co najmniej 2 wierzchołki")
        return

    if l < 1:
        print("-gnl: podaj co najmniej 1 krawędź")
        return

    matrix = [[0 for _ in range(l)] for _ in range(n)]

    # Na początku tworzymy listę wszystkich możliwych połączeń między
    # wierzchołami: [(0,1), (0,2), ..., (0,n-1), (1, 2), ..., (n-2, n-1)]
    # (wierzchołki numerujemy od 0 do n-1).
    avaliable_edges = [(i, j) for i in range(0, n) for j in range(i + 1, n)]

    if l > len(avaliable_edges):
        print("-gnl: za dużo krawędzi")
        return

    # Dokonujemy przetasowania w liście możliwych połączeń.
    rnd.shuffle(avaliable_edges)

    # Przechdzimy po kolumnach (krawędziach) macierzy incydencji
    # i uzupełniamy kolejne połączenia
    for i in range(0, l):
        edge = avaliable_edges[i]
        matrix[edge[0]][i] = 1
        matrix[edge[1]][i] = 1

    return matrix


def random_with_probability(n, p):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierz sąsiedztwa,
        z n wierzchołkami i p prawdopodobienstwem, które określa ile jest szans
        na to że pomiędzy dwoma wierzchołkami istnieje krawędź.
    """

    if p > 1 or p < 0:
        print("-gnp: prawdopodobieństwo nie mieści się w przedziale [0, 1].")
        return

    if n <= 1:
        print("-gnp: podaj co najmniej 2 wierzchołki")
        return

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # W algorytmie przechodzimy po górnej macierzy trójkątnej i losujemy
    # czy między wierzchołkami pojawia się krawędź.
    for i in range(0, n):
        for j in range(i + 1, n):
            if rnd.random() <= p:
                matrix[i][j] = matrix[j][i] = 1

    return matrix
