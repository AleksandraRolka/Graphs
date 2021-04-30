import random as r
import numpy as np
from utils import adj2inc
from task01 import seq_to_adj_matrix

def randomize_graph(n, sequence):

    """
    Funckja randomizująca graf prosty o zadanych wierzchołkach.
    Randomizowania grafu dokonuje się poprzez n-krotne zamienie krawędzi
    ab i cd na krawędzie ad i bc.
    Funckja zwraca jako wynik macierz incydencji.
    """

    # sprawdzamy czy z podanego ciagu można utworzyć graf
    matrix = seq_to_adj_matrix(sequence)

    if matrix is None:
        return

    # transponoujemy macierz incydencji bo chcemy żeby krawędzie były przedstawione jako wiersze
    matrix = np.transpose(np.array(adj2inc(matrix)))
    number_of_edges = len(matrix)

    max_attempts = number_of_edges ** 2
    
    while n and max_attempts: # dokonujemy n zamian pomiędzy krawędziam
        
        # dokonujemy losowania krawędzi które zostaną zamienione
        avaliable_edges = list(range(number_of_edges))
        r.shuffle(avaliable_edges)
        ab = avaliable_edges.pop()
        cd = avaliable_edges.pop()

        # pobranie indeksów wierzchołków na wylosowanych krawędziach
        a, b = [i for i, e in enumerate(matrix[ab]) if e == 1]
        c, d = [i for i, e in enumerate(matrix[cd]) if e == 1]

        # sprawdzamy czy wierzchołki nie zostały powtórzone
        if a == c or a == d or b == c or b == d:
            pass
        else:
            # zamiana krawędzi
            matrix[ab][b] = 0
            matrix[ab][d] = 1
            matrix[cd][d] = 0
            matrix[cd][b] = 1
            
            n -= 1
            
        max_attempts -= 1

    return np.transpose(matrix)
    
        
if __name__ == "__main__":
    print(randomize_graph(15, [2, 2, 2, 0]))