

def graph_from_edges(edges):
	matrix = [[ 0 for i in range(len(edges))] for j in range(len(edges))]
	for e in edges:
		matrix[e[0]][e[1]] = 1
		matrix[e[1]][e[0]] = 1
	return matrix
	
	
def printMatrix(matrix):
	for row in matrix:
		for el in row:
			print(el, end='  ')
		print()
			
def swap_rows(mtrx, i, j):
	temp = matrix[i][:]
	matrix[i][:] = matrix[j][:]
	matrix[j][:] = temp
	return matrix
		
def swap_columns(mtrx, i, j):
	for l in mtrx:
		l[i], l[j] = l[j], l[i]
	return matrix
		
if __name__ == "__main__":

	# edges = [(0, 1), (2, 0), (2, 1), (3, 0), (3, 1)]
	# graph = graph_from_edges(edges)
	# printMatrix(graph)
	
	seq = [2,0,2,2]
	matrix = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
	s1 = [sum(x) for x in matrix]
	
	print('seq = ',seq)
	print('sum = ',s1)
	

	printMatrix(matrix)
	print('---')
	
	for i in range(len(seq)):
		for j in range(len(seq)):
			if sum(matrix[i]) == seq[i]:
				pass
			else:
				for s in range(i+1,len(matrix)):
					if sum(matrix[s]) == seq[i]:
						swap_rows(matrix,i,s)
						swap_columns(matrix,i,s)

		
	
	printMatrix(matrix)
	# for i in range(len(matrix)):
		
		
	