import numpy as np
import random as rnd


def random_with_edges(n, l):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierzy incydencji
        z n wierzchołkami i l krawędziami.
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

    # Przechdzimy po kolumnach (krawędziach) macierzy incydencji
    # i uzupełniamy kolejne połączenia
    for i in range(0, l):
        edge = avaliable_edges[i]
        matrix[edge[0], i] = 1
        matrix[edge[1], i] = 1

    return matrix


def random_with_probability(n, p):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierz sąsiedztwa,
        z n wierzchołkami i p prawdopodobienstwem, które określa ile jest szans
        na to że pomiędzy dwoma wierzchołkami istnieje krawędź.
    """

    if p > 1 or p < 0:
        print("Prawdopodobieństwo nie mieści się w przedziale [0, 1].")
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
