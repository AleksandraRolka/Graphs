from enum import Enum

################################################################################################################################################

# Wypisanie macierzy
def print_matrix(matrix):
    repr = reprRecognizer(matrix)
    if repr in [GraphRepr.INC, GraphRepr.ADJ]:
        if repr == GraphRepr.ADJ:
            print("Macierz sąsiedztwa:")
        else:
            print("Macierz incydencji:")
        for row in matrix:
            for el in row:
                print(el, end=' ')
            print()
    elif repr == GraphRepr.LIST:
        print("Lista sąsiedztwa:")
        i = 0
        for row in matrix:
            i += 1
            print(i, ":", sep='', end=' ')
            for el in row:
                print(el, end=' ')
            print()
    else:
        print("Niepoprawny zapis")

# Z macierzy sąsiedztwa do listy sąsiedztwa
def adj2list(matrix):
    list_matrix = []
    for i in range(0, len(matrix)):
        list_matrix.append([])
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 1:
                list_matrix[i].append(j+1)
    return list_matrix

# Z macierzy sąsiedztwa do macierzy incydencji (kolejność kolumn jest inna niż w poleceniu zadania, ale same wyniki są ok)
def adj2inc(matrix):
    size = len(matrix)
    inc_matrix = [[] for i in range(0, size)]
    for i in range(0, size):
        for j in range(0, i + 1):
            if matrix[i][j] == 1:
                for k in range(0, size):
                    if k == i or k == j:
                        inc_matrix[k].append(1)
                    else:
                        inc_matrix[k].append(0)
    return inc_matrix

# Z listy sąsiedztwa do macierzy sąsiedztwa
def list2adj(graph_list):
    size = len(graph_list)
    adj_from_list = [[0 for i in range(0, size)] for i in range(0, size)]
    for i in range(0, size):
        for el in graph_list[i]: 
            adj_from_list[i][el-1] = 1
    return adj_from_list

# Z listy sąsiedztwa do macierzy incydencji
def list2inc(graph_list):
    size = len(graph_list)
    matrix_inc_from_list = [[] for i in range(0, size)]
    for i in range(0, size):
        for el in graph_list[i]:
            if (el-1) <= i:
                for k in range(0, size):
                    if k == i or k == (el-1):
                        matrix_inc_from_list[k].append(1)
                    else:
                        matrix_inc_from_list[k].append(0)
    return matrix_inc_from_list

# Z macierzy incydencji do macierzy sąsiedztwa
def inc2adj(inc_matrix):
    rows = len(inc_matrix)
    columns = len(inc_matrix[0])
    adj_matrix = [[0 for i in range(0, rows)] for i in range(0, rows)]
    for i in range(0, columns):
        dim =[]
        for j in range(0, rows):
            if (inc_matrix[j][i]) == 1:
                dim.append(j)
        adj_matrix[dim[0]][dim[1]] = 1
        adj_matrix[dim[1]][dim[0]] = 1
    return adj_matrix
    

# Z macierzy incydencji do listy sąsiedztwa
def inc2list(inc_matrix):
    rows = len(inc_matrix)
    columns = len(inc_matrix[0])
    list_from_inc = [[] for i in range(0, rows)]
    for i in range(0, columns):
        dim =[]
        for j in range(0, rows):
            if (inc_matrix[j][i]) == 1:
                dim.append(j)
        list_from_inc[dim[0]].append(dim[1]+1)
        list_from_inc[dim[1]].append(dim[0]+1)
    return list_from_inc



class GraphRepr(Enum):
    ADJ = 1
    INC = 2
    LIST = 3
    OTHER = 4

# Sprawdzenie czy reprezentacja jest listą sąsiedztwa
def isList(graph_repr):
    rows = len(graph_repr)
    if rows > 0:
        cols = len(graph_repr[0])
        for i in range(rows):
            # Sprawdzenie czy długość wiersza jest zmienna
            if len(graph_repr[i]) != cols:
                return True
            # Sprawdzenie czy występują wartości większe niż 1
            for j in graph_repr[i]:
                if j > 1:
                    return True
    return False

# Sprawdzenie czy reprezentacja jest macierzą sąsiedztwa
def isAdj(graph_repr):
    rows = len(graph_repr)
    if rows > 0:
        cols = len(graph_repr[0])
        # Sprawdzenie czy macierz jest kwadratowa
        if rows != cols:
            return False
        for i in range(rows):
            # Sprawdzenie czy na diagonali występują wartości niezerowe
            if graph_repr[i][i] != 0:
                return False
            for j in range(cols):
                # Sprawdzenie czy macierz jest symetryczna i składa się z wartości {0, 1}
                if graph_repr[i][j] != graph_repr[j][i] or graph_repr[i][j] not in [0, 1]:
                    return False
        return True
    return False

# Sprawdzenie czy reprezentacja jest macierzą incydencji
def isInc(graph_repr):
    rows = len(graph_repr)
    if rows > 0:
        cols = len(graph_repr[0])
        for i in range(cols):
            # Sprawdzenie czy suma w kolumnie jest równa 2
            sum = 0
            for j in range(rows):
                sum += graph_repr[j][i]
                # Sprawdzenie czy macierz składa się z wartości {0, 1}
                if graph_repr[j][i] not in [0, 1]:
                    return False
            if sum != 2:
                return False
        return True
    return False

def reprRecognizer(graph_repr):
    if isList(graph_repr):
        return GraphRepr.LIST
    if isAdj(graph_repr):
        return GraphRepr.ADJ
    if isInc(graph_repr):
        return GraphRepr.INC
    return GraphRepr.OTHER

################################################################################################################################################



if __name__ == "__main__":
    with open('adj.txt') as f:
        graph_repr = [[int(num) for num in line.split(' ')] for line in f]
    
    print_matrix(graph_repr)
    print()
    repr = reprRecognizer(graph_repr)

    if repr == GraphRepr.ADJ:
        print_matrix(adj2inc(graph_repr))
        print()
        print_matrix(adj2list(graph_repr))
    elif repr == GraphRepr.INC:
        print_matrix(inc2adj(graph_repr))
        print()
        print_matrix(inc2list(graph_repr))
    elif repr == GraphRepr.LIST:
        print_matrix(list2adj(graph_repr))
        print()
        print_matrix(list2inc(graph_repr))
