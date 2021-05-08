from utils import *


def adj_list_from_adj_matrix(adj_matrix):
	
	adj_list = []
	for i in range(len(adj_matrix)):
		temp = []
		for j in range(len(adj_matrix)):
			if adj_matrix[i][j] > 0:
				temp.append(j+1)
		adj_list.append(temp)
	
	return adj_list
	
def inc_matrix_from_adj_matrix(adj_matrix):
	
	edges = []
	adj_list = adj_list_from_adj_matrix(adj_matrix)
	for i in range(len(adj_matrix)):
		for j in range(len(adj_matrix[i])):
			if adj_matrix[i][j] > 0:
				edges.append((i+1,j+1,adj_matrix[i][j]))
	
	inc_matrix = [[0 for _ in range(len(edges))] for _ in range(len(adj_matrix))]
	
	for i in range(len(edges)):
		beg = edges[i][0]-1
		end = edges[i][1]-1
		
		inc_matrix[beg][i] = -edges[i][2]
		inc_matrix[end][i] =  edges[i][2]

	return inc_matrix
	

def random_digraph_with_probability(n, p):
	"""
		Funkcja zwraca wygenerowany losowo graf skierowany w postaci macierzy sąsiedztwa,
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

			  
	adj_matrix = random_digraph_with_probability(6,0.3)
	adj_list = adj_list_from_adj_matrix(adj_matrix)
	inc_matrix = inc_matrix_from_adj_matrix(adj_matrix)
	
	print("Wygenerowany losowy graf skierowany:")
	print("-------------------------------------------")
	print("macierz sąsiedztwa:")
	print_matrix(adj_matrix)
	print("lista sąsiedztwa:")
	for i in range(len(adj_list)):
		print('{}:  '.format(i),end='')
		for j in range(len(adj_list[i])):
			print(adj_list[i][j], end =' ')
		print()
	print("macierz incydencji:")
	print_matrix(inc_matrix)
	
		
	draw_graph_from_adj_matrix(adj_matrix, 'digraph')