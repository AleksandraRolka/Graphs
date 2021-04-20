from utils import *
from task01 import *
from task02 import *
from task03 import *

import numpy as np
import os, sys
import copy


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
		

def printMatrix(matrix):
	 for row in matrix:
            for el in row:
                print(el, end='  ')
            print()


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
	
	size = max( max( edges, key = lambda t: t[0] )[0], max( edges, key = lambda t: t[1] )[1] ) + 1
	matrix = [[ 0 for i in range(size)] for j in range(size)]
	for e in edges:
		matrix[e[0]][e[1]] = 1
		matrix[e[1]][e[0]] = 1

	return matrix

	
def is_bridge(edges, e):
	edge_list = copy.deepcopy(edges)
	edge_list.remove(e)
	graph = graph_from_edges(edge_list)
	comp = components(graph)
	if len(comp) == 1:
		return False
	else:
		return True
		