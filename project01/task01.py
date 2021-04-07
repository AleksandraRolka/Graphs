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


def adj2list(matrix):
    """
        Funkcja zamiany macierzy sąsiedztwa na liste sasiedztwa
        matrix - macierz sasiedztwa
    """
    list_matrix = []
    #przechodzimy petla po macierzy sasiedztwa
    for i in range(0, len(matrix)):
        #dla kazdego wiersza tworzymy liste w list_matrix
        list_matrix.append([])
        for j in range(0, len(matrix[i])):
            #jesli element macierzy sasiedztwa w wierszu jest rowny 1
			#dolaczamy do wiersza list_matrix wartosc (numer kolumny + 1) (+1 aby indeksowanie sie zgadzalo)
            if matrix[i][j] == 1:
                list_matrix[i].append(j+1)
    return list_matrix


def adj2inc(matrix):
    """
        Funkcja zamiany macierzy sasiedztwa na macierz incydyncji
        matrix - macierz sasiedztwa
    """
    size = len(matrix)
    inc_matrix = [[] for i in range(0, size)]
    #przechodzimy petla po trojkacie macierzy sasiedztwa, jesli element macierzy
	#rowny jest 1, w macierzy incydencji dodajemy kolumne, gdzie
	#jedynkami sa elementy o numerze wiersza rownym indeksom macierzy sasiedztwa - i,j
    for i in range(0, size):
        for j in range(0, i + 1):
            if matrix[i][j] == 1:
                for k in range(0, size):
                    if k == i or k == j:
                        inc_matrix[k].append(1)
                    else:
                        inc_matrix[k].append(0)
    return inc_matrix


def list2adj(graph_list):
    """
        Funkcja zamiany listy sasiedztwa na macierz seek
        graph_list - lista sasiedztwa
    """
    size = len(graph_list)
    adj_from_list = [[0 for i in range(0, size)] for i in range(0, size)]
    #przechodzimy petla po liscie, tworzymy macierz sasiedztwa,
	#nadajemy wartosc 1 elementom macierzy sasiedztwa o indeksach rownych
	#numerowi wiersza listy oraz wartosci aktualnego elementu pomniejszonego o jeden (aby zachowac indeksowanie)
    for i in range(0, size):
        for el in graph_list[i]:
            adj_from_list[i][el-1] = 1
    return adj_from_list


def list2inc(graph_list):
    """
        Funkcja zamiany listy na macierz incydencji
        graph_list - lista sasiedztwa
    """
    size = len(graph_list)
    matrix_inc_from_list = [[] for i in range(0, size)]
    #przechodzimy petla po liscie
    for i in range(0, size):
        for el in graph_list[i]:
            #aby nie powtarzac kolumn w macierzy incydencji
            if (el-1) <= i:
                #dodajemy kolumne z zerami
				#jedynkami w kolumnie sa elementy o indeksie numeru aktualnego
				#wiersza (i) oraz wartosci elementu (el-1) listy
                for k in range(0, size):
                    if k == i or k == (el-1):
                        matrix_inc_from_list[k].append(1)
                    else:
                        matrix_inc_from_list[k].append(0)
    return matrix_inc_from_list


def inc2adj(inc_matrix):
    """
        Funkcja zamiany macierzy incydencji na macierz sasiedztwa
        inc_matrix - macierz incydencji
    """
    rows = len(inc_matrix)
    columns = len(inc_matrix[0])
    adj_matrix = [[0 for i in range(0, rows)] for i in range(0, rows)]
    #szukamy w kolumnie inc_matrix jedynki i zapisujemy numery wierszy tych elementow w dim
	#nastepnie w adj_matrix elementy o indeksach z dim ustawiamy na 1
    for i in range(0, columns):
        dim =[]
        for j in range(0, rows):
            if (inc_matrix[j][i]) == 1:
                dim.append(j)
        adj_matrix[dim[0]][dim[1]] = 1
        adj_matrix[dim[1]][dim[0]] = 1
    return adj_matrix


def inc2list(inc_matrix):
    """
        Funkcja zamiany macierzy incydencji na liste sasiedztwa
        inc_matrix - macierz incydencji
    """
    rows = len(inc_matrix)
    columns = len(inc_matrix[0])
    list_from_inc = [[] for i in range(0, rows)]
    #szukamy w kolumnie inc_matrix jedynek i zapisujemy ich numery wierszy w dim
	#nastepnie w elemencie listy o numerze indeksu zapisanym w dim zapisujemy drugi indeks powiekszony o jeden
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

