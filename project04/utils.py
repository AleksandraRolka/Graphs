import math
import matplotlib.pyplot as plt
import networkx as nx

PI = math.pi

# Funkcje z poprzednich projektów 
################################################################################################################################################

def print_matrix(matrix):
	'''
		wypisuje maciersz w formie:
		np. 0  1  1
			1  0  1
			1  1  0         
	'''
	for row in matrix:
		for el in row:
			print('%4d' % el,end='')
		print() 
		
def print_matrix2(matrix):
	'''
		wypisuje maciersz w formie:
		np. 0  1  1
			1  0  1
			1  1  0         
	'''
	for row in matrix:
		for el in row:
			print('%4d' % el[1],end='')
		print() 
		
# TO FIX: - drawing selfloop edges

def draw_graph(nodes_num, edges, fname, colors = None, with_weights = False):
	"""
		Funkcja rysuje graf na podstawie trzech argumentów:
		- ilości wierzchołków (etykietowanie 1:ilość wierzchołków)
		- listy par krawędzi (od którego, do którego wierzchołka)
		- listy kolorów, na jakie zostaną pokolorowane kolejne spójne składowe
	"""
	fname = 'images/' + fname
	if colors == None:
		colors = '#b3ccff'
	# wyliczenie kąta do równomiernego rozłożenia wierzchołków na okręgu
	alpha = (2 * PI) / nodes_num
	# promień okręgu
	r = 15
	# współrzędne środka okręgu
	Sx, Sy = 20, 20
	# lista współrzędnych położenia wierzchołków
	positions = {}
	nodesize = 1500 / math.log(nodes_num, 10)

	# stworzenie pustego obiektu grafu, bez wierzchołków, bez krawędzi
	G = nx.MultiDiGraph()
	if nodes_num > 0:
		# dodanie listy wierzchołków
		# domyślnie kolejne wierzchołki jako ich etykiety mają kolejne liczby naturalne
		G.add_nodes_from(list(range(1, nodes_num + 1)))
		# dodanie listy krawędzi
		loop_edges = []
		for i in range(len(edges)):
			if edges[i][0] == edges[i][1]:
				loop_edges.append(edges[i])
			else:
				G.add_edge(edges[i][0],edges[i][1], weight=edges[i][2])

	for i in range(nodes_num):
		# wyliczenie współrzędnych położenia wierzcholków równomiernie na kole
		positions.update({(i + 1): (Sx + r * math.cos(i * alpha - PI / 2), Sy + r * math.sin(i * alpha + PI / 2))})

	options = {
	'arrowstyle': '-|>',
	'arrowsize': 18,
	}
	# wyrysowanie wierzchołków, krawędzi grafu na kole i zapis do pliku .png
	fig = plt.figure()
	nx.draw(G, arrows = True, **options, pos=positions, node_size=nodesize, node_color=colors,
			font_size= nodesize / 85, with_labels=True)
	
	for i in range(len(loop_edges)):
		G.add_edge(loop_edges[i][0],loop_edges[i][1], weight=loop_edges[i][2])
	nx.draw_networkx_edges(G, pos=positions, edgelist=loop_edges, arrowstyle="<|-", style="curved")

	if with_weights:
		l = nx.get_edge_attributes(G,'weight')	#tu błąd bo klucz jest trzyelementwoy ??
		labels = {}
		for key, value in l.items():
			labels[(key[0],key[1])] = value
		nx.draw_networkx_edge_labels(G, positions, edge_labels=labels, font_size=15, label_pos=0.6)
	
	plt.draw()
	fig.set_size_inches(12, 12)
	fig.savefig(fname)


def edges_from_adj_matrix(matrix):
	edges = []
	# przechodzimy pętlami po podanej macierzy sąsiedztwa
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			# zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami
			if matrix[i][j] != 0:
				edges.append((i+1, j+1,matrix[i][j]))
	return edges

def edges_from_adj_matrix_nodes_indexed_from_zero(matrix):
	edges = []
	# przechodzimy pętlami po podanej macierzy sąsiedztwa
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			# zapisujemy informacje o występujących połączeniach miedzy wierzchołkami, czyli krawędziami ideksująć wierzchołki od zera
			if matrix[i][j] != 0:
				edges.append((i, j,matrix[i][j]))
	return edges

	
def draw_graph_from_adj_matrix(matrix, fname, colors = None, with_weights = False):
	"""
		Funkcja rysuje graf na podstawie macierzy sąsiedztwa 
		(wykorzystuje funkcję draw_graph)
	"""
	# pierwszy wymiar macierzy daje nam liczbę wierzchołków
	nodes_num = len(matrix)
	edges = edges_from_adj_matrix(matrix)

	# na podstawie liczby wierzchołków oraz listy krawędzi wyrysowywujemy do pliku graficzną reprezentacje grafu
	draw_graph(nodes_num, edges, fname, colors, with_weights)
