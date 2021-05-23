from task03 import *
from utils import *
import copy
import numpy as np

def add_s(G, W):
    '''
        Funkcja dodająca nowy wierzchołek - łączący się z pozostałymi wierzchołkami krawędziami o wadze 0
        G - macierz sąsiedztwa
        W - macierz wag
    '''
    #skopiowanie G i W
    G_copy = copy.deepcopy(G)
    W_copy = copy.deepcopy(W)

    #dodanie wiersza jedynek do macierzy sąsiedztwa - dodany wierzcholek łączy się z pozostałymi
    new_row = np.array([1 for i in range(len(G))])
    G_copy = np.vstack([G_copy, new_row])

    #dodanie kolumny do macierzy sąsiedztwa- same zera ponieważ wierzcholki nie sa polaczone z nowo dodanym wierzcholkiem
    new_column = np.array([0 for i in range(len(G)+1)])
    G_copy = np.insert(G_copy, len(G), new_column, axis=1)

    #Dodanie wiersza i kolumny zer do macierzy wag
    new_column_w = np.array([0 for i in range(len(W)+1)])
    new_row_w = np.array([0 for i in range(len(W))])

    W_copy = np.vstack([W_copy, new_row_w])
    W_copy = np.insert(W_copy, len(W), new_column_w, axis=1)

    return G_copy,W_copy




def johnson(G, G_weights):
    '''
        Funkcja realizujaca algorytm Johnsona
        G - macierz sąsiedztwa
        G_weights - macierz wag
    '''
    #dodanie nowego wierzchołka z zerowymi wagami do pozostałych
    G_prim, W_prim= add_s(G, G_weights)
    check, d, p = BellmanFord(G_prim,  W_prim, len(G_prim) - 1)

    #sprawdzenie czy graf zawiera ujemny cykl za pomocą BellmanaForda
    if check == False:
        print("Graf zawiera ujemny cykl!")
        exit(-1)
    else:
        h = d
        W_copy = copy.deepcopy(W_prim)
        for i in range(len(G_prim)):
            for j in range(len(G_prim)):
                if G_prim[i][j] == 1:
                    #zmiana wag
                    W_copy[i][j] = W_prim[i][j] + h[i] - h[j]


        D = [[] for i in range(len(G))]

        for u in range(len(G)):
            D[u].extend(0 for _ in range(len(G)))
            
            distance,p = dijkstra(G_prim, W_copy, u)
            for v in range(len(G)):
                D[u][v] = distance[v] - h[u] + h[v]
        return D





if __name__ == "__main__":
    adj_matrix_unweighted = strongly_coherent_random_digraph(4,0.4)
    #print(adj_matrix_unweighted)
    adj_matrix = set_random_weight(copy.deepcopy(adj_matrix_unweighted),-5,10)	
    # adj_matrix = np.array([[ 0,  0,  0,  7],
    # [10,  0, -4, 0],
    # [ 0,  0,  0,  1],
    # [ 0,  9,  0,  0]])

    # adj_matrix_unweighted = np.array([[0, 0, 0, 1],
    # [1, 0, 1, 0],
    # [0, 0, 0, 1],
    # [0, 1, 0, 0]])

    print(adj_matrix)
    print(adj_matrix_unweighted)
    print(johnson(adj_matrix_unweighted, adj_matrix))
        
