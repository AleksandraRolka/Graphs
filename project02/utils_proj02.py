from task03 import print_components
import numpy as np
import sys
import os
import copy

''' 
    FUNKCJE POMOCNICZE DO PROJEKTU 2 
'''
#################################################################################################################

class HiddenPrints:
    '''
        klasa pozwala na uruchamianie funkcji 
        z pominięciem funkcji print wewnątrz nich
    '''
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
    
       
def print_matrix(matrix):
    ''' wypisuje maciersz w formie:
        np. 0  1  1
            1  0  1
            1  1  0         
    '''
    for row in matrix:
        for el in row:
            print('%4d' % el,end='')
        print()


def matrix_remove_zeros(matrix):
    '''
        usuwa z macierzy sąsiedztwa 
        wiersze i kolumny 
        zawierające same zera
    '''
    data = np.array(copy.deepcopy(matrix))
    data = data[~np.all(data == 0, axis=1)]
    idx = np.argwhere(np.all(data[..., :] == 0, axis=0))
    data = np.delete(data, idx, axis=1)
    return data


def components_list_and_max(graph):
    '''
        funkcja zwraca indeks maksymalnej składowej 
        oraz listę wszystkich składowych
        pomijając print-y funkcji 'print_components'
    '''
    with HiddenPrints():
        max, comps = print_components(graph)
        return comps, max


def swap_rows(matrix, i, j):
    '''
        zamienia w macierzy wiersze i z j
    '''
    temp = matrix[i][:]
    matrix[i][:] = matrix[j][:]
    matrix[j][:] = temp
    return matrix

def swap_columns(matrix, i, j):
    '''
        zamienia w macierzy kolumny i z j
    '''
    for l in matrix:
        l[i], l[j] = l[j], l[i]
    return matrix
    

def rearange_matrix_by_seq(matrix, seq):
    '''
        dostosowywuje kolejności wierszy, kolumn grafu 
        do kolejności stopni wierzchołków podanego ciągu
    '''
    
    for i in range(len(seq)):
        for j in range(len(seq)):
            if sum(matrix[i]) == seq[i]:
                pass
            else:
                for s in range(i+1, len(matrix)):
                    if sum(matrix[s]) == seq[i]:
                        swap_rows(matrix, i, s)
                        swap_columns(matrix, i, s)

    return matrix