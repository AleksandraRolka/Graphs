from utils import *
import numpy as np
import random as rnd


def adj_list_from_adj_matrix(adj_matrix):
	'''
		Na wejście przyjmuje macierz sąsiedztwa digrafu,
		zwraca listę sąsiedztwa podanego digrafu.
	'''
	adj_list = []
	for i in range(len(adj_matrix)):
		# dla każdego wierzchołka sporządzamy listę wierzchołków,
		# do których prowadzą krawędzie rozpoczynające się w danym wierzchołku
		temp = []
		for j in range(len(adj_matrix)):
			if adj_matrix[i][j] > 0:
				temp.append(j+1)
		adj_list.append(temp)
	
	return adj_list
	
def inc_matrix_from_adj_matrix(adj_matrix):
	'''
		Na wejście przyjmuje macierz sąsiedztwa digrafu,
		zwraca macierz incydencji podanego digrafu.
	'''
	edges = []
	# Przechodząc przez macierz sąsiedztwa 
	# zapisujemy wszystkie krawędzie wraz z ich wagami
	for i in range(len(adj_matrix)):
		for j in range(len(adj_matrix[i])):
			if adj_matrix[i][j] > 0:
				edges.append((i+1,j+1,adj_matrix[i][j]))
	
	# Wiedząc ile jest wszystkich krawędzi oraz mając rozmiar macierzy sąsiedztwa, 
	# znamy wymiary macierzy incydencji
	# Inicjumemy macierz incydencji zerami
	inc_matrix = [[0 for _ in range(len(edges))] for _ in range(len(adj_matrix))]
	
	# Następnie nadpisujemy elementy macierzy odpowiednimi wagami krawędzi,
	# początek z wagą ujemną, koniec z dodatnią
	for i in range(len(edges)):
		beg = edges[i][0]-1
		end = edges[i][1]-1
		
		inc_matrix[beg][i] = -edges[i][2]
		inc_matrix[end][i] =  edges[i][2]

	return inc_matrix
	

def random_digraph_with_probability(n, p):
	'''
		Funkcja zwraca wygenerowany losowo graf skierowany w postaci macierzy sąsiedztwa,
		z n wierzchołkami i p prawdopodobienstwem, które określa ile jest szans
		na to że pomiędzy dwoma wierzchołkami istnieje krawędź.
	'''

	if p > 1 or p < 0:
		print("Prawdopodobieństwo nie mieści się w przedziale [0, 1].")
		return
	if n <= 1:
		print("Podaj co najmniej 2 wierzchołki")
		return

	matrix = np.zeros((n, n), dtype=int)

	# ponieważ jest to digraf, przechodzimy po całej macierzy i losujemy
	# czy od/do wierzchołka pojawia się krawędź
	for i in range(0, n):
		for j in range(0, n):
			if rnd.random() <= p and i!=j:
				matrix[i][j] = 1
				
	return matrix


if __name__ == "__main__":
  
	adj_matrix = random_digraph_with_probability(6,0.4)
	adj_list = adj_list_from_adj_matrix(adj_matrix)
	inc_matrix = inc_matrix_from_adj_matrix(adj_matrix)
	
	print("Wygenerowany losowy graf skierowany:")
	print("-------------------------------------------")
	print("macierz sąsiedztwa:")
	print_matrix(adj_matrix)
	print("lista sąsiedztwa:")
	for i in range(len(adj_list)):
		print('{}:  '.format(i+1),end='')
		for j in range(len(adj_list[i])):
			print(adj_list[i][j], end =' ')
		print()
	print("macierz incydencji:")
	print_matrix(inc_matrix)
		
	draw_graph_from_adj_matrix(adj_matrix, 'digraph1')
