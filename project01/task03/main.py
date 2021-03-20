import numpy as np
import random as rnd

def losowy_z_krawedziami(n, l):

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

    macierz = np.zeros((n, l), dtype=int)

    # Na początku tworzymy listę wszystkich możliwych połączeń między
    # wierzchołami: [(0,1), (0,2), ..., (0,n-1), (1, 2), ..., (n-2, n-1)]
    # (wierzchołki numerujemy od 0 do n-1).
    mozliwe_polaczenia = [ (i, j) for i in range(0, n) for j in range(i+1, n) ]

    # Dokonujemy przetasowania w liście możliwych połączeń.
    rnd.shuffle(mozliwe_polaczenia)

    # Przechddzimy po kolumnach (krawędziach) macierzy incydencji
    # i uzupełniamy kolejne połączenia
    for i in range(0, l):
        krawedz = mozliwe_polaczenia[i]
        macierz[ krawedz[0], i ] = 1
        macierz[ krawedz[1], i ] = 1

    return macierz


def losowy_z_prawdopodobienstwem(n, p):

    """
    Funkcja zwraca wygenerowany losowo graf w postaci macierz incydencji,
    z n wierzchołkami i p prawdopodobienstwem, które określa ile jest szans 
    na to że pomidzy dwoma wierzchołkami istnieje krawędź.
    """

    if p > 1 or p < 0:
        print("Prawdopodieństwo nie mieści się w przedziale [0, 1].")
        return

    if n <= 1:
        print("Podaj co najmniej 2 wierzchołki")
        return

    macierz = np.zeros((n, n), dtype=int)

    # W algorytmie przechodzimy po górnej macierzy trójkątnej i losujemy
    # czy między wierzchołkami pojawia się krawędź.
    for i in range(0, n):
        for j in range(i + 1, n):
            if rnd.random() <= p:
                macierz[i][j] = macierz[j][i] = 1
    
    return macierz
