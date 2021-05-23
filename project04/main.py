from task01 import *
from task02 import *
from task03 import *
from task04 import *
import sys

class LackOfNecessaryArg(Exception):
    pass


def main():

    args = sys.argv[1:]
    filename_in = None
    filename_out = None
    graph = None
    p = None
    n = None
    a = None
    b = None

    
    if len(args) > 0:
        try:
            if len(args) == 1:
                if "-help" in args:
                    print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
LISTA DOSTĘPNYCH KOMEND:
[-help]                                         - wyświetla listę dostępnych komend
[-random_digraph_with_probability]              - generuje losowy graf skierowany
[-kosaraju]                                     - algorytm kosaraju - zwraca silnie spójne składowe digrafu
[-bellmann_ford]                                - algorytm Bellmanna-Forda - zwraca macierz odległości
[-johnson]                                      - algorytm Johnsona - zwraca macierz odległości
*** Aby sprawdzić z jakimi argumentami wywołuje się dany program uruchom z "-help", np. "python3 main.py -kosaraju -help" ***
*** Aby zapisać graficzną reprezentacje wynikowego grafu:
[-fileout filename]                             - [filename] nazwa pliku, do którego ma zostać zapisany obraz grafu w formacie png
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
                elif "-random_digraph_with_probability" in args:
                    print("----\n  Wywołaj -random_digraph_with_probability -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-kosaraju" in args:
                    print("----\n  Wywołaj -kosaraju -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-bellmann_ford" in args:
                    print("----\n  Wywołaj -bellmann_ford -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-johnson" in args:
                    print("----\n  Wywołaj -johnson -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                else:
                    raise LackOfNecessaryArg
        
            elif "-random_digraph_with_probability" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -random_digraph_with_probability:
[-n n -p p]                             - generuje losowy graf skierowany o [n] wierzchołkach i [p] prawdopodobieństwie wystąpienia krawędzi
dodatkowo [-fileout filename]           - zapisze graf do pliku [filename] w folderze graph_examples
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-kosaraju" in args and "-help" in args:
                 print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -kosaraju:
[-n n -p p]                             - zwraca silnie spójne skladowe dla losowego grafu skierowanego o [n] wierzchołkach i [p] prawdopodobieństwie wystąpienia krawędzi
[-filein filename]                      - zwróci silnie spójne składowe dla grafu zapisanego w pliku [filename] w folderze graphs_examples 
                                          (graf w pliku powinien być w postaci macierzy sąsiedztwa) 
dodatkowo [-fileout filename]           - zapisze graf do pliku [filename] w folderze graph_examples
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-bellmann_ford" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -bellmann_ford:
[-n n -p p -a a -b b]                   - znajduje najkrótsze ścieżki dla losowego grafu skierowanego o [n] wierzchołkach 
                                          i [p] prawdopodobieństwie wystąpienia krawędzi
                                          o losowych wagach z przedziału [a, b]
[-default]                              - znajduje najkrótsze ścieżki dla losowego grafu skierowanego o domyślnych parametrach: [n = 6] wierzchołkach i [p = 0.8] prawdopodobieństwie
                                          wystąpienia krawędzi o losowych wagach z przedziału [a = -5, b = 10]
dodatkowo [-fileout filename]           - zapisze graf do pliku [filename] w folderze graph_examples
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-johnson" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -johnson:
[-n n -p p -a a -b b]                   - znajduje najkrótsze ścieżki między parami wierzchołków dla losowego grafu skierowanego o [n] wierzchołkach 
                                          i [p] prawdopodobieństwie wystąpienia krawędzi
                                          o losowych wagach z przedziału [a, b]
[-default]                              - znajduje najkrótsze ścieżki dla losowego grafu skierowanego o domyślnych parametrach: [n = 6] wierzchołkach i [p = 0.8] prawdopodobieństwie
                                          wystąpienia krawędzi o losowych wagach z przedziału [a = -5, b = 10]
dodatkowo [-fileout filename]           - zapisze graf do pliku [filename] w folderze graph_examples
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
                if "-p" in args:
                    idx = args.index("-p")
                    p = float(args[idx+1])     
                if "-filein" in args:
                    idx = args.index("-filein")
                    filename_in = args[idx+1]
                    with open("graphs_examples/"+filename_in) as f:
                        graph = [
                            [int(num) for num in line.split(' ')] for line in f]
                
                # ------------------------------------------------------------------------------------------------------------------------------  

                if args[0] == '-random_digraph_with_probability':
                    if p is None or n is None:
                        raise LackOfNecessaryArg
                    else:
                        adj_matrix = random_digraph_with_probability(n, p)
                        adj_list = adj_list_from_adj_matrix(adj_matrix)
                        inc_matrix = inc_matrix_from_adj_matrix(adj_matrix)
                        print("Wygenerowany losowy graf skierowany:")
                        print("-------------------------------------------")
                        print("macierz sąsiedztwa:")
                        print_matrix(adj_matrix)
                        print("lista sąsiedztwa:")
                        for i in range(len(adj_list)):
                            print('{}:  '.format(i+1),end='')
                            for j in range(len(adj_list[i])):
                                print(adj_list[i][j], end =' ')
                            print()
                        print("macierz incydencji:")
                        print_matrix(inc_matrix)
                        if filename_out is not None:    
                            draw_graph_from_adj_matrix(adj_matrix, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')

                # ------------------------------------------------------------------------------------------------------------------------------  

                if args[0] == "-kosaraju":
                    if filename_in is None:
                        if p is None or n is None:
                            raise LackOfNecessaryArg
                        else:
                            graph = random_digraph_with_probability(n, p)
                            comp = kosaraju(graph)
                            print_comp(comp)
                    else:
                        comp = kosaraju(graph)
                        print_comp(comp)
                    if filename_out is not None:    
                            draw_graph_from_adj_matrix(graph, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')

                 # ------------------------------------------------------------------------------------------------------------------------------  
                    
                if args[0] == "-bellmann_ford":
                    if any(item is None for item in [a,b,n,p]):
                        adj_matrix_unweighted = strongly_coherent_random_digraph()
                        adj_matrix = set_random_weight(adj_matrix_unweighted)	
                       
                    else:
                        adj_matrix_unweighted = strongly_coherent_random_digraph(n, p)
                        adj_matrix = set_random_weight(adj_matrix_unweighted, a, b)	

                    dist_matrix = []
                    for i in range(len(adj_matrix)):
                        check, dist, p = (BellmanFord(adj_matrix_unweighted, adj_matrix, i))
                        if check == False:
                            print("Graf zawiera ujemny cykl")
                            sys.exit(0)
                        else:
                            dist_matrix.append(dist)

                    print("Losowy silnie spójny digraf ważony:")
                    print_matrix(adj_matrix)
                    print("Macierz odległości:")
                    print_matrix(dist_matrix)
                    
                    if filename_out is not None:    
                            draw_graph_from_adj_matrix(adj_matrix, filename_out, with_weights = True)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')

                # ------------------------------------------------------------------------------------------------------------------------------  
                
                if args[0] == "-johnson":
                    if any(item is None for item in [a,b,n,p]):
                        adj_matrix_unweighted = strongly_coherent_random_digraph()
                        adj_matrix = set_random_weight(copy.deepcopy(adj_matrix_unweighted))

                    else:
                        adj_matrix_unweighted = strongly_coherent_random_digraph(n, p)
                        adj_matrix = set_random_weight(copy.deepcopy(adj_matrix_unweighted), a, b)

                    print("Losowy silnie spójny digraf ważony")
                    print_matrix(adj_matrix)
                    print("Macierz odległości:")
                    print_matrix(johnson(adj_matrix_unweighted, adj_matrix))

                    if filename_out is not None:    
                            draw_graph_from_adj_matrix(adj_matrix, filename_out, with_weights = True)
                            print('\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')

                # ------------------------------------------------------------------------------------------------------------------------------  

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