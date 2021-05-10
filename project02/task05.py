from task02 import randomize_graph

def random_k_regular_graph(n, k):
    """
        Funcja przyjmuje jako argument parametry k-regularnego grafu:
        k oraz liczbę wierzchołków n.

        Funkcja zwraca zrandomizowany graf w postaci macierzy incydencji.
    """
    seq = [ k for i in range(n) ]
    return randomize_graph(100, seq)[1]
