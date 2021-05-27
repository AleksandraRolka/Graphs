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
            if len(args) == 1:
                if "-help" in args:
                    print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
LISTA DOSTĘPNYCH KOMEND:
[-help]                                         - wyświetla listę dostępnych komend
[-is_graphic_seq]                               - sprawdza czy sekwencja jest ciągiem graficznym
[-randomize_graph]                              - randomizuje [n] razy graf prosty
[-largest_connected_component]                  - znajduje największą spójną składową graf
[-random_eulerian_graph]                        - generuje losowy graf Eulera i znajduje w nim cykl Eulera
[-random_k_regular_graph]                       - generuje losowy graf k-regularny
[-is_hamiltonian_graph]                         - sprawdza czy graf jest hamiltonowski, jeśli tak to zwraca cykl Hamiltona

*** Aby sprawdzić z jakimi argumentami wywołuje się dany program uruchom z "-help", np. "python3 main.py -is_graphic_seq -help" ***
*** Aby zapisać graficzną reprezentacje wynikowego grafu:
[-fileout filename]                             - [filename] nazwa pliku, do którego ma zostać zapisany obraz grafu w formacie png
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
                elif "-is_graphic_seq" in args:
                    print(
                        "----\n  Wywołaj -is_graphic_seq -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-randomize_graph" in args:
                    print(
                        "----\n  Wywołaj -randomize_graph -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-largest_connected_component" in args:
                    print(
                        "----\n  Wywołaj -largest_connected_component -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-random_eulerian_graph" in args:
                    print(
                        "----\n  Wywołaj -random_eulerian_graph -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-random_k_regular_graph" in args:
                    print(
                        "----\n  Wywołaj -random_k_regular_graph -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                elif "-is_hamiltonian_graph" in args:
                    print(
                        "----\n  Wywołaj -is_hamiltonian_graph -help aby zobaczyć jakich argumentów wymaga komenda\n---")
                else:
                    raise LackOfNecessaryArg

            elif "-is_graphic_seq" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -is_graphic_seq:
[-seq seq]                  - sprawdza czy podana na wejściu sekwencja [seq] (separator=' ') jest ciągiem graficznym
[-filein filename]          - sprawdza czy sekwencja z pliku graph_representations/[filename] jest ciągiem graficznym
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-randomize_graph" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -randomize_graph:
[-seq seq -n n]             - randomizuje [n] razy graf prosty o zadanym ciągu [seq] stopni wierzchołków
[-filein filename -n n]     - randomizuje [n] razy graf prosty o zadanym ciągu stopni wierzchołków, z pliku graph_representations/[filename]
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-largest_connected_component" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -largest_connected_component:
[-filein filename] - znajduje największą spójną składową grafu, znajdującego się w pliku graph_representations/[filename] 
                                                  (możliwe postacie wejściowego grafu: macierz sąsiedztwa, macierz incydencji, lista sąsiedztwa, ciąg)
[-gnl -n n -l l]   - znajduje największą spójną składową wygenerowanego losowego grafu o [n] wierzchołkach i [l] krawędziach
[-gnp -n n -p p]   - znajduje największą spójną składową wygenerowanego losowego grafu o [n] wierzchołkach i [p] prawdop. wystąpienia krawędzi,
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-random_eulerian_graph" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -random_eulerian_graph:
[-n n]          - generuje losowy graf Eulera o [n] wierzchołkach i znajduje w nim cykl Eulera
--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-random_k_regular_graph" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -random_k_regular_graph:
[-n n -k k]     - generuje losowy graf [k]-regularny o [n] wierzchołkach

--------------------------------------------------------------------------------------------------------------------------------------------------------------
""")
            elif "-is_hamiltonian_graph" in args and "-help" in args:
                print("""
--------------------------------------------------------------------------------------------------------------------------------------------------------------
PODKOMENDY DO -is_hamiltonian_graph:
[-filein filename]        - sprawdza czy graf (postać:lista sąsiedztwa) znajdujący się w pliku jest hamiltonowski, jeśli tak to zwraca cykl Hamiltona
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
                    seq = [int(args[i]) for i in range(idx+1, end)]
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
                        ''' sprawdzenie czy podany ciag liczb jest ciagiem graficznym '''
                        check = degree_seq(seq, len(seq))
                        print()
                        print(seq)
                        print('Podany ciąg jest graficzny.')
                        ''' utworzenie macierzy sasiedztwa na podstawie ciagu liczb '''
                        adj_matrix = seq_to_adj_matrix(seq)
                        if adj_matrix is None:
                            return
                        print(
                            '\nGraf w postaci macierzy sąsiedztwa, utworzonej na podstawie zadanego ciągu:')
                        print_matrix(adj_matrix)

                        ''' zapis reprezentacji graficznej do pliku w razie potrzeby '''
                        if filename_out is not None:
                            draw_graph_from_adj_matrix(
                                adj_matrix, filename_out)
                            print(
                                '\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------
                elif args[0] == '-randomize_graph':
                    if seq is None or n is None:
                        raise LackOfNecessaryArg
                    else:
                        try:
                            ''' randomizacja grafu prostego o zadanym ciągu stopni wierzchołków '''
                            orginal, randomized = randomize_graph(n, seq)
                        except Exception as e:
                            return
                        print('\nPierwotnie utworzony graf:')
                        print_matrix(orginal)
                        print('\nGraf po randomizacjach:')
                        print_matrix(randomized)

                        ''' zapis reprezentacji graficznej do pliku w razie potrzeby '''
                        if filename_out is not None:
                            draw_graph_from_incid_matrix(
                                randomized, filename_out)
                            print(
                                '\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------
                elif args[0] == '-largest_connected_component':
                    if graph is None:
                        raise LackOfNecessaryArg
                    else:
                        (repr, graph) = repr_recognizer(graph)
                        ''' konwersja wejściowego grafu do macierzy sąsiedztwa '''
                        if repr == GraphRepr.INC:
                            graph = inc2adj(graph)
                        elif repr == GraphRepr.LIST:
                            graph = list2adj(graph)
                        elif repr == GraphRepr.SEQ:
                            graph = seq_to_adj_matrix(graph)
                        if repr != GraphRepr.OTHER:
                            '''Wypisuje wejściowy graf w postaci macierzy sąsiedztwa'''
                            print('Graf w postaci macierzy sąsiedztwa:')
                            print_matrix(graph)
                            ''' Wyznacza wraz z wypisaniem na ekran spójne składowe oraz numer tej największej '''
                            print('\nSpójne składowe grafu:')
                            print_components(graph)
                            ''' zapis reprezentacji graficznej do pliku w razie potrzeby '''
                            if filename_out is not None:
                                draw_components(graph, filename_out)
                                print(
                                    '\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
                        else:
                            print(
                                'Podano niepoprawne dane wejściowe.\n(Możliwe postacie grafu wejściowego: macierz sąsiedztwa, lista sąsiedztwa, macierz incydencji, ciąg graficzny')
            # ------------------------------------------------------------------------------------------------------------------------------
                elif args[0] == '-random_eulerian_graph':
                    if n is None:
                        raise LackOfNecessaryArg
                    else:
                        if n < 3:
                            print('Warunek ( n>=3 ) niespełniony')
                            return
                        else:
                            ''' wygenerowanie losowego grafu Eulera o n wierzchołkach + znalezienie w nim cyklu Eulera '''
                            seq, graph, cycle = gen_random_eulerian_graph_find_cycle(
                                n)
                            print(
                                "\n\nWygenerowano losowy ciąg (grafu eulerowskiego):\n{}".format(seq))
                            print("\nGraf Eulera w postaci macierzy sąsiedztwa:")
                            print_matrix(graph)
                            print("\nCykl Eulera wygenerowanego grafu:")
                            for i in range(len(cycle)-1):
                                print('{0} -- '.format(cycle[i]), end='')
                            print(cycle[len(cycle)-1])

                            ''' zapis reprezentacji graficznej do pliku w razie potrzeby '''
                            if filename_out is not None:
                                draw_graph_from_adj_matrix(graph, filename_out)
                                print(
                                    '\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------
                elif args[0] == '-random_k_regular_graph':
                    if n is None or k is None:
                        raise LackOfNecessaryArg
                    else:
                        try:
                            ''' wygenerowanie losowego grafu k-regularnego o n-wierzchołkach '''
                            graph = random_k_regular_graph(n, k)
                        except Exception as e:
                            return
                        print(
                            "\nWygenerowany losowy graf {}-regularny o {} wierchołkach:\n(macierz incydencji)".format(k, n))
                        print_matrix(graph)

                        ''' zapis reprezentacji graficznej do pliku w razie potrzeby '''
                        if filename_out is not None:
                            draw_graph_from_incid_matrix(graph, filename_out)
                            print(
                                '\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
            # ------------------------------------------------------------------------------------------------------------------------------
                elif args[0] == '-is_hamiltonian_graph':
                    if graph is None:
                        raise LackOfNecessaryArg
                    else:
                        # zmniejszenie wartosci o jeden, aby numerowanie od zera się zgadzało
                        copy_graph = copy.deepcopy(graph)
                        copy_graph = [[x-1 for x in graph[i]]
                                      for i in range(0, len(graph))]
                        ''' sprawdzenie czy podany graf jest hamiltonowski, jeśli tak, zwraca cykl Hamiltona '''
                        cycle = find_hamilton_cycle(copy_graph)
                        if cycle is not None:
                            print(
                                '\n\nPodany graf jest grafem hamiltonowskim.\nZnaleziony cykl Hamiltona: ', cycle)
                        else:
                            print('Zadany graf nie posiada cyklu Hamiltona.')

                        ''' zapis reprezentacji graficznej do pliku w razie potrzeby '''
                        if filename_out is not None:
                            draw_graph_from_adj_list(graph, filename_out)
                            print(
                                '\nGraficzną reprezentację grafu zapisano w pliku image/' + filename_out + '.png')
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
