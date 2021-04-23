from utils import *
import copy

def find_hamilton_cycle(graph, v = 0, stack = []):
    '''Funkcja znajdujaca cykl hamiltona

    Argumenty:
        graph - lista sasiedztwa grafu
        v - sprawdzany wierzcholek
        stack - stos dodanych wierzcholkow
    
    Zwraca:
        [x+1 for x in stack] - stos powiekszony o jeden - nasz znaleziony cykl
        None - jesli nie znajdzie cyklu

    '''
    if v not in stack:
        stack.append(v)
    
        if len(stack) == len(graph):
            #sprawdzenie czy ostatni wierzcholek znajduje sie w sasiadach wierzcholka startowego
            if stack[-1] in graph[stack[0]]:
                stack.append(stack[0])
                return [x+1 for x in stack]
            else:
                stack.pop()
                return None
        
        # jesli stos nie zawiera wszystkich wierzcholkow
        #wywolujemy rekurencyjnie funkcje dla wszystkich
        #nieodwiedzonych sasiadow ostatniego ze stosu
        for neighbor in graph[v]:
            stack_backup = copy.deepcopy(stack)
            result = find_hamilton_cycle(graph, neighbor, stack_backup)
            if result is not None:
                return result


if __name__ == "__main__":
    filename = "graph_representations/adj_list_hamilton.txt"
    graph = readGraphFromFile(filename)

    #zmniejszenie wartosci o jeden, aby numerowanie od zera dzialalo
    graph = [[x-1 for x in graph[i]] for i in range(0, len(graph))]
    result = find_hamilton_cycle(graph)
    if result is not None:
        print('Znaleziono cykl Hamiltona: ', result)
    else:
        print('Zadany graf nie posiada cyklu Hamiltona.')
