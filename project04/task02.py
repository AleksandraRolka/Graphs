import numpy

def DFS_visit(i, G, d, f, t):
    '''
        Funkcja przeszukąjąca graf w głąb
        i - aktualny wierzchołek
        G - macierz sąsiedztwa grafu
        d - wektor czasu odwiedzenia wierzchołka
        f - wektor czasu przetworzenia wierzchołka
        t - chwila czasowa
        
    '''
    t = t + 1
    d[i] = t

    #przeglądamy wierzchołki będące sąsiadami i
    for j in range(0, len(G)):
        if G[i][j] == 1:
            if d[j] == -1:
                DFS_visit(j, G, d, f, t)
    t = t + 1
    #dodajemy wierzchołek do stosu
    f.append(i)


def components(nr, i, G, comp):
    '''
        Funkcja przypisująca numer silnie spójnej składowej wierzchołkowi
        nr - numer silnie spójnej składowej
        i - numer wierzchołka
        G - macierz sąsiedztwa grafu
        comp - lista numerów silnie spójnych składowych
    '''
    for j in range(0, len(G)):
        if G[i][j] == 1:
            if comp[j] == -1:
                comp[j] = nr
                components(nr, j, G, comp)



def kosaraju(G):
    '''
        Funkcja realizująca algorytm kosaraju do znajdowanie silnie spójnych składowych
        G - macierz sąsiedztwa grafu
    '''
    G = numpy.array(G)
    size = len(G)

    #czasy odwiedzenia wierzchołków
    d = []
    #czas przetworzenia wierzchołków
    f = []
    for i in range(size):
        d.append(-1)
    
    #inicjalizacja czasu
    t = 0
    for i in range(0, size):
        if d[i] == -1:
            DFS_visit(i, G, d, f, t)
    
    G = numpy.transpose(G)
    nr = 0
    comp = [-1 for i in range(size)]
   

    for i in f[::-1]:
        if comp[i] == -1:
            nr = nr + 1
            comp[i] = nr
            components(nr, i, G, comp)

    return comp


def print_comp(comp):
    '''
        Funkcja wypisującą silnie spójne składowe
        comp - lista przypisanych numerów silnie spójnych składowych do wierzchołków
    '''
    groups = {}
    for i in range(len(comp)):
        if str(comp[i]) not in groups:
            groups[str(comp[i])] = [i+1]
        else:
            groups[str(comp[i])].append(i+1)            
    for key, value in groups.items():
        print("Silnie spójna składowa : " + str(value))



if __name__ == "__main__":
    with open("graphs_examples/graph.txt") as f:
                graph = [
                    [int(num) for num in line.split(' ')] for line in f]

    comp = kosaraju(graph)
    print_comp(comp)