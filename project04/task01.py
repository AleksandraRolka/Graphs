from utils import *



def random_digraph_with_probability(n, p):
    """
        Funkcja zwraca wygenerowany losowo graf w postaci macierzy sąsiedztwa,
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

    # Ponieważ jest to digraf, przechodzimy po całej macierzy i losujemy
    # czy od/do wierzchołka pojawia się krawędź
    for i in range(0, n):
        for j in range(0, n):
            if rnd.random() <= p:
                matrix[i][j] = 1

    return matrix




if __name__ == "__main__":

			  
	graph = random_digraph_with_probability(6,0.3)
	print_matrix(graph)
	draw_graph_from_adj_matrix(graph, 'digraph')