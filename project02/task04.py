from utils import *
from utils_proj02 import *

from task01 import *
from task02 import *
from task03 import *

import random as rnd
import os, sys
import copy


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
	rnd.shuffle(seq)
	
	return seq
	
	
def only_one_comp(graph):
	comps,max = components_list_and_max(graph)
	comps.remove(comps[max-1])
	for x in comps:
		if x > 1:
			return False
		
	return True
		

def find_next_node(edges, curr,first):
	not_bridges = []
	bridges = []
	
	for i in range(len(edges)):
		if edges[i][0] == curr or edges[i][1] == curr:
			if is_bridge(edges, edges[i]):
				bridges.append(edges[i])
			else:
				not_bridges.append(edges[i])

	with_first_in_edges = [ e for e in edges if e[0]==first or e[1]==first]

	if not_bridges:
		inx = rnd.randint(0,(len(not_bridges)-1))
		if not_bridges[inx][0] == curr:
			return not_bridges[inx][1]
		else:
			return not_bridges[inx][0]
	else: 
		if len(with_first_in_edges) > 0:
			inx = rnd.randint(0,(len(bridges)-1))
			if bridges[inx][0] == curr:
				return bridges[inx][1]
			else:
				return bridges[inx][0]
		else:
			if 1 < len(bridges):
				inx = rnd.randint(1,(len(bridges)-1))
				if bridges[inx][0] == curr:
					return bridges[inx][1]
				else:
					return bridges[inx][0]
			else:
				False
		



def find_eulerian_cycle(graph):
	finish = False
	inc_list =  adj2list(graph)
	edges = []
	for i in range(len(inc_list)):
		for j in range(len(inc_list[i])):
			if (i+1 != inc_list[i][j]):
				k = inc_list[i][j]
				if ((i+1, k) not in edges) and (( k, i+1)  not in edges):
					edges.append((i+1, k))
	
	visited_edges, visited_vertices = [], []
	(first,second) = edges[0]
	visited_edges.append(edges[0])
	visited_vertices.append(first)
	visited_vertices.append(second)
	prev = first
	curr = second
	edges.remove(edges[0])
	
	while edges:
		prev = curr
		if len(edges) == 1:
			visited_edges.append((prev, first))
			visited_vertices.append(first)
			finish = True
			break
		curr = find_next_node(edges, curr,first)
		if curr == None:
			break;
		else:
			visited_edges.append((prev, curr))
			visited_vertices.append(curr)
			if (prev, curr) in edges:
				edges.remove((prev, curr))
			else:
				edges.remove((curr,prev))	
	
	if not finish:
		find_eulerian_cycle(graph)
	return visited_vertices
	

	

def task04():
	
	n = 0
	n =  int(input("\nPodaj liczbę n (>=3) wierzchołów, dla których utworzony zostanie graf eulerowski:\n"))
	while n < 3:
		n =  int(input("Nieprawidłowa wartość n. Spróbuj ponownie: "))
	

	seq = gen_eulerian_seq(n)
	graph = seq_to_adj_matrix(seq)
	graph = rearange_matrix_by_seq(graph,seq)
	
	while not only_one_comp(graph):
		seq = gen_eulerian_seq(n)
		graph = seq_to_adj_matrix(seq)
		graph = rearange_matrix_by_seq(graph,seq)
		

	seq_subgraph = []
	csg_labels = []
	
	for i in range(len(seq)):
		if seq[i] != 0:
			seq_subgraph.append(seq[i])
			csg_labels.append(i+1)

	# spójna część grafu 'graph' ( graf graph bez wierzchołków izolowanych )
	subgraph = matrix_remove_zeros(graph)
	cycle_list = find_eulerian_cycle(subgraph)




				
	print("\n__Wygenerowany losowy ciąg (grafu eulerowskiego): ", seq)
	print("__Graf Eulera w postaci macierzy sąsiedztwa:")
	printMatrix(graph)
	print("__Graficzna wersja grafu zapisana w pliku: images/eulerian_graph.png\n")
	draw_graph_from_adj_matrix(graph, "eulerian_graph.png")
			
	

	print("__Cykl Eulera wygenerowanego grafu:")
	for i in range(len(cycle_list)-1):
		print('{0} -- '.format(csg_labels[cycle_list[i]-1]), end='')
	print(csg_labels[0])

		
	
	

		
		
		