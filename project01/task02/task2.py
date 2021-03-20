import math
import networkx as nx
import matplotlib.pyplot as plt

PI = math.pi


#----------------------------------------------------------------------------------

"""
	Funkcja rysuje graf na podstawie dwóch argumentów: 
	- ilości wierzchołków (etykietowanie 1-ilość wierzchołków)
	- listy par krawędzi (od którego, do którego wierzchołka)
"""
def draw_graph(nodes_num,edges):

	alpha = (2 * PI) / nodes_num
	r = 15
	Sx,Sy = 20,20
	positions = {}
	
	G = nx.Graph()
	if nodes_num > 0:
		G.add_nodes_from(list(range(1,nodes_num+1)))
		G.add_edges_from(edges)
	
	for i in range(nodes_num):
		positions.update({ (i + 1) : ( Sx + r * math.cos(i * alpha - PI/2), Sy + r * math.sin(i * alpha + PI/2) ) })

	
	fig = plt.figure()
	nx.draw(G, pos=positions, node_size=1200*20/nodes_num, node_color='#b3ccff', font_size=(1200*20/nodes_num)/85, with_labels=True)
	plt.draw()
	fig.set_size_inches(12, 12)
	fig.savefig("graf_wizualizacja.png")


#----------------------------------------------------------------------------------

"""
	Funkcja rysuje graf na podstawie macierzy sąsiedztwa
	(wykorzystuje funkcję draw_graph)
"""
def draw_graph_from_adj_matrix(matrix):

	size1 = len(matrix)
	size2 = len(matrix[0])
	
	nodes_num = size1
	edges=[]
	
	for	i in range(size1):
		for j in range(size2):
			if matrix[i][j] == 1:
				edges.append((i+1,j+1))

	draw_graph(nodes_num,edges)
	
"""
	Funkcja rysuje graf na podstawie listy sąsiedztwa
	(wykorzystuje funkcję draw_graph)
"""	
def draw_graph_from_adj_list(adjlist):

	size1 = len(adjlist)
	nodes_num = size1
	edges=[]
	
	for	i in range(size1):
		for j in range(len(adjlist[i])):
			if adjlist[i][j]:
				edges.append((i+1,adjlist[i][j]))

	draw_graph(nodes_num,edges)

"""
	Funkcja rysuje graf na podstawie macierzy incydencji 
	(wykorzystuje funkcję draw_graph)
"""	
def draw_graph_from_incid_matrix(matrix):

	size1 = len(matrix)
	size2 = len(matrix[0])
	
	nodes_num = size1
	edges=[]
	
	for j in range(size2):
		ends = []
		for	i in range(size1):
			if matrix[i][j] == 1:
				ends.append(i+1)
		edges.append((ends[0],ends[1]))
	

	draw_graph(nodes_num,edges)



#-------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	with open('data.txt') as f:
		matrix = [[int(num) for num in line.split(' ')] for line in f]
	
	
	# draw_graph_from_adj_matrix(matrix)
	# draw_graph_from_adj_list(matrix)
	draw_graph_from_incid_matrix(matrix)

	
	