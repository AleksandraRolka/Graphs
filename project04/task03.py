from task01 import random_digraph_with_probability
from task02 import kosaraju
from utils import *
import random as rnd
import numpy as np


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
	

if __name__ == "__main__":

	adj_matrix = strongly_coherent_random_digraph(6,0.4)
	adj_matrix = set_random_weight(adj_matrix,-5,10)
	
	draw_graph_from_adj_matrix(adj_matrix, 'digraph3',with_weights=True)

	print(adj_matrix)	