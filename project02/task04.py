from utils import *
from task01 import *
from task02 import *
from task03 import *
import random as rnd
import os, sys


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def gen_random_seq_of_even_num(n):
	deg = []
	seq = []
	k = int((n +1) // 2) * 2
		
	for i in range(k):
		if i%2 == 0:
			deg.append(i)
	
	e,d = 0,0
	for i in range(n):
		if e < 3:
			while d == 0:
				d = rnd.choice(deg)
		else:
			d = rnd.choice(deg)
		e += 1	
		seq.append(d)

	return seq


def gen_eulerian_seq(n):
	seq = gen_random_seq_of_even_num(n)
	while not( degree_seq(seq, len(seq)) ):
		seq = gen_random_seq_of_even_num(n)
	
	return seq
	
	
def printMatrix(matrix):
	 for row in matrix:
            for el in row:
                print(el, end='  ')
            print()
			
			
def largerCompIndex(graph):
	# with HiddenPrints():
	inx = printComponents(graph)
	return inx
		

if __name__ == "__main__":
	
	n = 0
	n =  int(input("\nPodaj liczbę n (>=3) wierzchołów, dla których utworzony zostanie graf eulerowski:\n"))
	while n < 3:
		n =  int(input("Nieprawidłowa wartość n. Spróbuj ponownie: "))
	
	seq = gen_eulerian_seq(n) 
	graph = seq_to_adj_matrix(seq)
	# graph = randomize_graph(100,seq)
	
	print("\n__Wylosowane stopnie wierzchołków:\n", seq)
	print("\n__Macierz sąsiedztwa wygenerowanego grafu:")
	printMatrix(graph)
	draw_graph_from_adj_matrix(graph, "eulerian_graph.png")
	print("\n__Graficzna wersja grafu zapisana w pliku 'images/eulerian_graph.png'.\n")

	seq_cons_subgraph = []
	csg_labels = []
	
	for i in range(len(seq)):
		if seq[i] != 0:
			seq_cons_subgraph.append(seq[i])
			csg_labels.append(i+1)
	
	
	# print(seq_cons_subgraph)
	# print(csg_labels)
	
	# spójna część grafu 'graph' ( graf graph bez wierzchołków izolowanych )
	cons_subgraph = seq_to_adj_matrix(seq_cons_subgraph)

		
		
		
		
		
		
		