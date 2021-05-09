from task01 import random_digraph_with_probability
from task02 import kosaraju
from utils import *
import random as rnd
import numpy as np
from math import inf
import sys


def only_one_comp(graph):
	'''
		Sprawdza czy graf (macierz sąsiedztwa) 
		zawiera tylko jedną silnie spójną składową 
	'''
	comp = kosaraju(graph)
	for i in range(len(comp)):
		if comp[i] != 1:
		   return False
	return True

def set_random_weight(adj_matrix, a, b):
	'''
		W podanym grafie (macierzy sąsiedztwa) występujacym krawędziom
		przypisuje losowe wagi z podanego przedziału [a,b]
	'''
	for i in range(len(adj_matrix)):
		for j in range(len(adj_matrix)):
			if adj_matrix[i][j] == 1:
				tmp=rnd.randint(a, b)
				while tmp == 0:
					tmp=rnd.randint(a, b)
				adj_matrix[i][j] = tmp
	return adj_matrix
	
def strongly_coherent_random_digraph(n, p):
	'''
		Generuje losowy silnie spójny digraf
	'''
	adj_matrix = random_digraph_with_probability(n,p)
	while not only_one_comp(adj_matrix):
		adj_matrix = random_digraph_with_probability(n,p)
	return adj_matrix
	
	
def BellmanFord(graph,v0):
	'''
		Znajduje najkrótsze ścieżeki od danego wierzchołka.
		Zwraca listę odległóśći od wierzchołka źródłowego 
		do pozostałych wierzchołków.
	'''
	edges = edges_from_adj_matrix_indexinf_from_zero(graph)
	V = len(graph)
	# inicjalizacja odleglosci do wszystkich wierzchołków jako nieskończ.
	d = [inf] * V
	# inicjalizacja odlegości do wierzchołka źródłowego jako 0
	d[v0] = 0	
	
	# Relaksacja krawędzi V-1 razy
	for i in range(1, V-1):
		for e in edges:
			u = e[0]
			v = e[1]
			w = e[2]
			# print('{}   {}   {}'.format(d[v],d[v],w))
			if  d[v] > d[u] + w:
				d[v] = d[u] + w
 
	# Sprawdza czy są cykle o ujemnej wadze, jeśli tak, 
	# kończy program wypisując wcześniej informacje o ujemnym cyklu
	for e in edges:
		u = e[0]
		v = e[1]
		w = e[2]
		if d[v] > d[u] + w:
			print("Graf zawiera ujemny cykl")
			return sys.exit(-1)
		
	return d;
	


if __name__ == "__main__":

	adj_matrix = strongly_coherent_random_digraph(4,0.4)
	adj_matrix = set_random_weight(adj_matrix,-2,10)	
	dist_matrix = []
	for i in range(len(adj_matrix)):
		dist_matrix.append(BellmanFord(adj_matrix,i))
		
	draw_graph_from_adj_matrix(adj_matrix, 'digraph3',with_weights=True)
	print("Losowy silnie spójny digraf ważony:")
	print_matrix(adj_matrix)
	print("Macierz odległości:")
	print_matrix(dist_matrix)
	