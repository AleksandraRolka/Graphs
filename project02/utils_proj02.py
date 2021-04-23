from utils import *
from task01 import *
from task02 import *
from task03 import *

import numpy as np
import os, sys
import copy

''' 
	FUNKCJE POMOCNICZE DO PROJEKTU 2 
'''

# funkcje wykorzystane w task04
#############################################################################
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
		

def printMatrix(matrix):
    for row in matrix:
        print("    ",end='')
        for el in row:
            print(el, end='  ')
        print("\n",end='')


def swap_rows(matrix, i, j):
	temp = matrix[i][:]
	matrix[i][:] = matrix[j][:]
	matrix[j][:] = temp
	return matrix
		
		
def swap_columns(matrix, i, j):
	for l in matrix:
		l[i], l[j] = l[j], l[i]
	return matrix
		
		
def matrix_remove_zeros(matrix):
	data = np.array(copy.deepcopy(matrix))
	data = data[~np.all(data == 0, axis=1)]
	idx = np.argwhere(np.all(data[..., :] == 0, axis=0))
	data = np.delete(data, idx, axis=1)
	return data

def graph_from_edges(edges):
	
	size = max( max( edges, key = lambda t: t[0] )[0], max( edges, key = lambda t: t[1] )[1] )
	matrix = [[ 0 for i in range(size)] for j in range(size)]
	for e in edges:
		matrix[e[0]-1][e[1]-1] = 1
		matrix[e[1]-1][e[0]-1] = 1

	return matrix

def components_list_and_max(graph):
	with HiddenPrints():
		max, comps = printComponents(graph)
		return comps,max
		
def is_bridge(edges, e):
	edge_list = copy.deepcopy(edges)
	graph = graph_from_edges(edge_list)
	graph[e[0]-1][e[1]-1] = 0
	graph[e[1]-1][e[0]-1] = 0
	comp = components(graph)
	
	if sum(comp) == len(comp):
		return False
	else:
		return True
		
		
	

def rearange_matrix_by_seq(matrix, seq):
	for i in range(len(seq)):
		for j in range(len(seq)):
			if sum(matrix[i]) == seq[i]:
				pass
			else:
				for s in range(i+1,len(matrix)):
					if sum(matrix[s]) == seq[i]:
						swap_rows(matrix,i,s)
						swap_columns(matrix,i,s)
	
	return matrix
		
#############################################################################
		