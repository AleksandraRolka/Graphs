from task01 import *
from task02 import *
from task03 import *
from task04 import *
from task05 import *
from task06 import *
import sys


class LackOfNecessaryArg(Exception):
    pass


def main():

    args = sys.argv[1:]
    filename_in = None
    filename_out = None
    graph = None
    seq = None
    n = None
    l = None
    p = None
    k = None
    
    if len(args) > 0:
        try:
            
            if "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
LISTA DOSTĘPNYCH KOMEND:
[-help]                                         - wyświetla listę dostępnych komend
[-is_graphic_seq -seq seq]                      - sprawdza czy podana na wejściu sekwencja [seq] (separator=' ') jest ciągiem graficznym
[-is_graphic_seq -filein filename]              - sprawdza czy sekwencja z pliku graph_representations/[filename] jest ciągiem graficznym
[-randomize_graph -seq seq -n n]                - randomizuje [n] razy graf prosty o zadanym ciągu [seq] stopni wierzchołków
[-randomize_graph -filein filename -n n]        - randomizuje [n] razy graf prosty o zadanym ciągu stopni wierzchołków, z pliku graph_representations/[filename]
[-largest_connected_component -filein filename] - znajduje największą spójną składową grafu, znajdującego się w pliku graph_representations/[filename]
[-largest_connected_component -gnl -n n -l l]   - znajduje największą spójną składową wygenerowanego losowego grafu o [n] wierzchołkach i [l] krawędziach
[-largest_connected_component -gnp -n n -p p]   - znajduje największą spójną składową wygenerowanego losowego grafu o [n] wierzchołkach i l krawędziach,
[-random_eulerian_graph -n n]                     - generuje losowy graf Eulera o [n] wierzchołkach i znajduje w nim cykl Eulera
[-random_k_regular_graph -n n -k k]             - generuje losowy graf [k]-regularny o [n] wierzchołkach
[-is_hamiltonian_graph -filein filename]        - sprawdza czy graf jest hamiltonowski, jeśli tak to zwraca cykl Hamilton
[-fileout filename]                             - plik, do którego ma zostać zapisany obraz grafu            

UWAGI:  
 - Pierwszy argument jest stały, musi być to jeden z podanych: -is_graphic_seq / -randomize_graph / -largest_connected_component / 
                                                               -random_eulerian_graph / -random_k_regular_graph / -is_hamiltonian_graph
 - Pozostałe argumenty ruchome, kolejność nie jest istotna.
 - Powyżej pokazane są jakie argumenty są konieczne w zależności od pierwszego argumentu, który wskazuje cel programu.
--------------------------------------------------------------------------------------------------------------------------------------------------------------                     
                    """)
            else:
                
                # ---------------------------------------------------
                # Parsowanie podanych argumentów wywołania programu 
                # ---------------------------------------------------
                if "-fileout" in args:
                    idx = args.index("-fileout")
                    filename_out = args[idx+1]
                if "-n" in args:
                    idx = args.index("-n")
                    n = int(args[idx+1])
                if "-l" in args:
                    idx = args.index("-l")
                    l = int(args[idx+1])
                if "-p" in args:
                    idx = args.index("-p")
                    p = float(args[idx+1])
                if "-k" in args:
                    idx = args.index("-k")
                    k = int(args[idx+1])
                    
                if "-filein" in args:
                    idx = args.index("-filein")
                    filename_in = args[idx+1]
                    with open("graph_representations/"+filename_in) as f:
                        graph = [
                            [int(num) for num in line.split(' ')] for line in f]
                        if args[0] == '-is_graphic_seq' or args[0] == '-randomize_graph':
                            seq = graph[0]
                elif "-seq" in args:
                    idx = args.index("-seq")
                    end = None
                    if "-n" in args:
                        end = args.index("-n")
                    elif "-fileout" in args:
                        end = args.index("-fileout")
                    elif len(args) > idx+1:
                        end = len(args)
                    if end is None:
                        raise LackOfNecessaryArg
                    seq = [ int(args[i]) for i in range(idx+1,end) ]   
                elif "-gnl" in args:     
                    if n is not None and l is not None:
                        graph = random_with_edges(n, l)
                elif "-gnp" in args:     
                    if n is not None and p is not None:
                        graph = random_with_probability(n, p)
                    

        # ------------------------------------------------------------------------------------------------------------------------------
        # Wywołanie odpowiednich funkcji z plików 'task0%.py' w zależności od pierwszego argumentu, który wskazuje na rodzaj zadania 
        # ------------------------------------------------------------------------------------------------------------------------------    
                if args[0] == '-is_graphic_seq':
                    if seq is None:
                        raise LackOfNecessaryArg
                    else:
                        check = degree_seq(seq, len(seq))
                        print('\n')
                        print(seq)
                        print('Podany ciąg jest graficzny.')
                        adj_matrix = seq_to_adj_matrix(seq)
                        if adj_matrix is None:
                            return
                        print('\nGraf w postaci macierzy sąsiedztwa, utworzonej na podstawie zadanego ciągu:')
                        print_matrix(adj_matrix)
                        
                        if filename_out is not None:
                            draw_graph_from_adj_matrix(adj_matrix, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------    
                elif args[0] == '-randomize_graph':
                    if seq is None or n is None:
                        raise LackOfNecessaryArg
                    else:
                        try:
                            orginal, randomized = randomize_graph(n, seq)
                        except Exception as e:
                            return
                        print('\nPierwotnie utworzony graf:')
                        print_matrix(orginal)
                        print('\nGraf po {} randomizacjach:'.format(n))
                        print_matrix(randomized)
                        
                        if filename_out is not None:
                            draw_graph_from_incid_matrix(randomized, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')                    
            # ------------------------------------------------------------------------------------------------------------------------------        
                elif args[0] == '-largest_connected_component':
                    if graph is None:
                        raise LackOfNecessaryArg
                    else:
                        (repr, graph) = repr_recognizer(graph)
                        if repr == GraphRepr.INC:
                            graph = inc2adj(graph)
                        elif repr == GraphRepr.LIST:
                            graph = list2adj(graph)
                        elif repr == GraphRepr.SEQ:
                            graph = seq_to_adj_matrix(graph)
                        if repr != GraphRepr.OTHER:
                            print_components(graph)
                            
                        if filename_out is not None:
                            draw_components(graph, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------    
                elif args[0] == '-random_eulerian_graph':
                    if n is None:
                        raise LackOfNecessaryArg
                    else:
                        if n < 3:
                            print('Warunek ( n>=3 ) niespełniony')
                            return
                        else:
                            seq, graph, cycle = gen_random_eulerian_graph_find_cycle(n)
                            print("\n\nWygenerowano losowy ciąg (grafu eulerowskiego):\n{}".format(seq))
                            print("\nGraf Eulera w postaci macierzy sąsiedztwa:")
                            print_matrix(graph)
                            print("\nCykl Eulera wygenerowanego grafu:")
                            for i in range(len(cycle)-1):
                                print('{0} -- '.format(cycle[i]), end='')
                            print(cycle[len(cycle)-1])
                            
                            if filename_out is not None:
                                draw_graph_from_adj_matrix(graph, filename_out)
                                print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------    
                elif args[0] == '-random_k_regular_graph':
                    if n is None or k is None:
                        raise LackOfNecessaryArg
                    else:
                        try:
                            graph = random_k_regular_graph(n, k)
                        except Exception as e:
                            return
                        print("\nWygenerowany losowy graf {}-regularny o {} wierchołkach:\n(macierzy incydencji)".format(k,n))
                        print_matrix(graph)
                        
                        if filename_out is not None:
                            draw_graph_from_incid_matrix(graph, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------    
                elif args[0] == '-is_hamiltonian_graph':
                    if graph is None:
                        raise LackOfNecessaryArg
                    else:
                        # zmniejszenie wartosci o jeden, aby numerowanie od zera dzialalo
                        graph = [[x-1 for x in graph[i]] for i in range(0, len(graph))]
                        cycle = find_hamilton_cycle(graph)
                        if cycle is not None:
                            print('\n\nPodany graf jest grafem hamiltonowskim.\nZnaleziony cykl Hamiltona: ', cycle)
                        else:
                            print('Zadany graf nie posiada cyklu Hamiltona.')
							
                        if filename_out is not None:
                            draw_graph_from_adj_list(graph, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
                else:
                    raise LackOfNecessaryArg

        except LackOfNecessaryArg:
            print("Konieczne argumenty nie zostały podane")
        except ValueError:
            print("Niepoprawny typ argumentu")
            return
        except IndexError:
            print("Podano nieprawidłową ilość argumentów")
            return
        except FileNotFoundError:
            print("Podany plik wejściowy nie istnieje")
        except Exception as e:
            print(e)        
    
    else:
        print(
            "Nie podano żadnych argumentów\nLista akceptowanych argumentów dostępna pod komendą [-help]")
        return
        

if __name__ == "__main__":
    main()