from task01 import *
from task02 import *
from task03 import *
from task04 import *
from task05 import *

import sys


class LackOfNecessaryArg(Exception):
    pass

def main():

    args = sys.argv[1:]
    n = None
    a = None
    b = None
    filename_out = None
    input_graph = None
    
    if len(args) > 0:
        try:
            
            if "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
LISTA DOSTĘPNYCH KOMEND:
[-help]                                             - wyświetla listę dostępnych komend
[-random_coherent_weighted_graph -n n -out out]     - generuje losowy graf spójny o [n] wierzchołkach z wagami krawędzi w zakresie [1, 10]]
[-random_coherent_weighted_graph -n n -a a -b b -out out]  - generuje losowy graf spójny o [n] wierzchołkach z wagami krawędzi w zakresie [[a], [b]]
[-dijkstra -n n -out out]                           - algorytm dijkstry dla losowego grafu o [n] wierzchołkach
[-dijkstra -graph graph -out out]                   - algorytm dijkstry dla podanego przez użytkownika grafu w postaci macierzy sąsiedztwa
[-distance_matrix -n n -out out]                    - tworzy macierz odległości dla losowego grafu o [n] wierzchołkach
[-distance_matrix -graph graph -out out]            - tworzy macierz odległości dla podanego przez użytkownika grafu w postaci macierzy sąsiedztwa
[-graph_centers -n n -out out]                      - wyszukuje centrum i centrum minimax dla losowego grafu o [n] wierzchołkach
[-graph_centers -graph graph -out out]              - wyszukuje centrum i centrum minimax dla podanego przez użytkownika grafu w postaci macierzy sąsiedztwa
[-minimal_spanning_tree -n n -out out]              - tworzy minimalne drzewo rozpinające dla losowego grafu o [n] wierzchołkach
[-minimal_spanning_tree -graph graph -out out]      - tworzy minimalne drzewo rozpinające dla podanego przez użytkownika grafu w postaci macierzy sąsiedztwa

--------------------------------------------------------------------------------------------------------------------------------------------------------------                     
                    """)
            else:
                
                # ---------------------------------------------------
                # Parsowanie podanych argumentów wywołania programu 
                # ---------------------------------------------------
                if "-out" in args:
                    idx = args.index("-out")
                    filename_out = args[idx+1]
                else:
                    raise LackOfNecessaryArg()
                if "-n" in args:
                    idx = args.index("-n")
                    n = int(args[idx+1])
                if "-a" in args:
                    idx = args.index("-a")
                    a = int(args[idx+1])
                if "-b" in args:
                    idx = args.index("-b")
                    b = float(args[idx+1])

                    
                if "-graph" in args:
                    idx = args.index("-graph")
                    filename_in = args[idx+1]
                    with open("graph_representations/"+filename_in) as f:
                        input_graph = [
                            [int(num) for num in line.split(' ')] for line in f]
                    

        # ------------------------------------------------------------------------------------------------------------------------------
        # Wywołanie odpowiednich funkcji z plików 'task0%.py' w zależności od pierwszego argumentu, który wskazuje na rodzaj zadania 
        # ------------------------------------------------------------------------------------------------------------------------------    
                if args[0] == '-random_coherent_weighted_graph':
                    if n is None:
                        raise LackOfNecessaryArg
                    else:
                        if a is None and b is None:
                            random_graph = generate_random_coherent_weighted_graph(n)
                        else:
                            if b <= a:
                                raise "b nie może być mniejsze od a"
                            random_graph = generate_random_coherent_weighted_graph(n, a, b)

                        print()
                        print('Wylosowany został następujący graf: (postać macierzy sąsiedztwa)')

                        print_matrix(random_graph)
                        
                        if filename_out is not None:
                            draw_graph_from_adj_matrix(random_graph, filename_out)
                            print('\nGraficzną reprezentację grafu zapisano w pliku images/' + filename_out + '.png')

            # ------------------------------------------------------------------------------------------------------------------------------    
                elif args[0] == '-minimal_spanning_tree':

                    if input_graph is None and n > 0:
                        random_graph = generate_random_coherent_weighted_graph(n)
                        g = random_graph
                        print("Graf został wylosowany... Trwa szukanie mimalnego drzewa rozpinającego")

                    elif n is None and len(input_graph) > 0:
                        g = input_graph
                        print("Pobrano macierz sąsiedztwa z pliku... Trwa szukanie minimalnego drzewa rozpinającego")

                    else:
                        raise "Podaj albo [n] liczbę wierzchołków do wygenerowania lub plik z gotowym grafem [graph]"
                        
                    mst, cost = kruskal_algorithm(g)
                    print("Algortm szukania minimalnego drzewa rozpinającego zakończony")
                    print(f"Suma wag krawęzi MDR wynosi {cost}")
                    
                    if filename_out is not None:
                        draw_graph_with_mst(g, mst, filename_out)
                        print('\nGraficzną reprezentację grafu zapisano w pliku images/' + filename_out + '.png')
                    
                elif args[0] == '-dijkstra':

                    if input_graph is None and n > 0:
                        random_graph = generate_random_coherent_weighted_graph(n)
                        g = random_graph
                        print("Graf został wylosowany...")

                    elif n is None and len(input_graph) > 0:
                        g = input_graph
                        print("Pobrano macierz sąsiedztwa z pliku...")

                    else:
                        raise "Podaj albo [n] liczbę wierzchołków do wygenerowania lub plik z gotowym grafem [graph]"
                        
                    (d, p) = dijkstra(g)
                    print_dijkstra(d, p)
                    
                    if filename_out is not None:
                        print('\nGraficzną reprezentację grafu zapisano w pliku images/' + filename_out + '.png')
                        draw_graph_from_adj_matrix(g, filename_out)

                elif args[0] == '-distance_matrix':

                    if input_graph is None and n > 0:
                        random_graph = generate_random_coherent_weighted_graph(n)
                        g = random_graph
                        print("Graf został wylosowany...")

                    elif n is None and len(input_graph) > 0:
                        g = input_graph
                        print("Pobrano macierz sąsiedztwa z pliku...")

                    else:
                        raise "Podaj albo [n] liczbę wierzchołków do wygenerowania lub plik z gotowym grafem [graph]"
                        
                    dm = get_distance_matrix(g)

                    print("Otrzymaliśmy następującą macierz odległości")
                    print_matrix(dm)

                    if filename_out is not None:
                        print('\nGraficzną reprezentację grafu zapisano w pliku images/' + filename_out + '.png')
                        draw_graph_from_adj_matrix(g, filename_out)

                elif args[0] == '-graph_centers':

                    if input_graph is None and n > 0:
                        random_graph = generate_random_coherent_weighted_graph(n)
                        g = random_graph
                        print("Graf został wylosowany...")

                    elif n is None and len(input_graph) > 0:
                        g = input_graph
                        print("Pobrano macierz sąsiedztwa z pliku...")

                    else:
                        raise "Podaj albo [n] liczbę wierzchołków do wygenerowania lub plik z gotowym grafem [graph]"
                        
                    (center_idx, center_val, minimax_center_idx,
                    minimax_center_val) = find_graph_centers(g)
                    print("Centrum = ", center_idx+1,
                        " (suma odległości: ", center_val, ")", sep='')
                    print("Centrum minimax = ", minimax_center_idx+1,
                        " (odległość od najdalszego: ", minimax_center_val, ")", sep='')

                    if filename_out is not None:
                        print('\nGraficzną reprezentację grafu zapisano w pliku images/' + filename_out + '.png')
                        draw_graph_from_adj_matrix(g, filename_out)

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
