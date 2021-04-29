from task01 import *
from task02 import *
from task03 import *
import sys


def main():
    args = sys.argv[1:]
    alen = len(args)
    graph_repr = None
    filename_out = None
    repr = None
    # Parsowanie podanych argumentów wywołania programu
    if alen > 0:
        try:
            if "-help" in args:
                print("""
--------------------------------------------------------------------------------
Lista dostępnych komend:
[-help]             - wyświetla listę dostępnych komend
[-gnl n l]          - generuje graf losowy o [n] wierzchołkach i [l] krawędziach
[-gnp n p]          - generuje graf losowy o [n] wierzchołkach i l krawędziach,
                      których ilość zależy od prawdopodobieństwa [p]
[-filein filename]  - wczytuje reprezentację grafu z pliku o nazwie filename
[-fileout filename] - plik, do którego ma zostać zapisany obraz grafu            
[-repr repr]        - reprezentacja grafowa, według której dane wejściowe
                      mają zostać zinterpretowane
                      akceptowane reprezentacje: [adj], [inc], [list]

Przykład wywołania programu:
python3 main.py -gnl 10 15 -fileout graf -repr inc                      
--------------------------------------------------------------------------------                     
                    """)
            else:
                if "-gnl" in args:
                    idx = args.index("-gnl")
                    n = int(args[idx+1])
                    l = int(args[idx+2])
                    graph_repr = random_with_edges(n, l)
                elif "-gnp" in args:
                    idx = args.index("-gnp")
                    n = int(args[idx+1])
                    p = float(args[idx+2])
                    graph_repr = random_with_probability(n, p)
                elif "-filein" in args:
                    idx = args.index("-filein")
                    filename = args[idx+1]
                    with open(filename) as f:
                        graph_repr = [
                            [int(num) for num in line.split(' ')] for line in f]
                else:
                    print("Nie podano żadnego źródła danych")

                if "-fileout" in args:
                    idx = args.index("-fileout")
                    filename_out = args[idx+1]
                else:
                    print("Nie podano nazwy pliku wyjściowego")

                if "-repr" in args:
                    idx = args.index("-repr")
                    repr_name = args[idx+1]
                    if repr_name == "adj":
                        repr = GraphRepr.ADJ
                    elif repr_name == "inc":
                        repr = GraphRepr.INC
                    elif repr_name == "list":
                        repr = GraphRepr.LIST

        except IndexError:
            print("Podano nieprawidłową ilość argumentów")
            return
        except ValueError:
            print("Niepoprawny typ argumentu")
            return
        except FileNotFoundError:
            print("Podany plik wejściowy nie istnieje")
        except Exception as e:
            print(e)

        if graph_repr is None or filename_out is None:
            return
        # Jeśli repr nie została ustalona lub jest niezgodna z wynikiem funkcji is_[repr] to zostaje wykorzystana funkcja repr_recognizer
        if (repr == None) or (repr == GraphRepr.ADJ and not is_adj(graph_repr)) or (repr == GraphRepr.INC and not is_inc(graph_repr)) or (repr == GraphRepr.LIST and not is_list(graph_repr)):
            repr = repr_recognizer(graph_repr)
        if not filename_out.endswith(".png"):
            filename_out += ".png"

        print("\nNa wejściu:")
        print("---------------------------------------------------")
        print_matrix(graph_repr, repr)
        print()

        print("\nPozostałe reprezentacje grafu:")
        print("---------------------------------------------------")

        if repr == GraphRepr.ADJ:
            print_matrix(adj2inc(graph_repr))
            print()
            print_matrix(adj2list(graph_repr))
            draw_graph_from_adj_matrix(graph_repr, filename_out)
        elif repr == GraphRepr.INC:
            print_matrix(inc2adj(graph_repr))
            print()
            print_matrix(inc2list(graph_repr))
            draw_graph_from_incid_matrix(graph_repr, filename_out)
        elif repr == GraphRepr.LIST:
            print_matrix(list2adj(graph_repr))
            print()
            print_matrix(list2inc(graph_repr))
            draw_graph_from_adj_list(graph_repr, filename_out)

    else:
        print(
            "Nie podano żadnych argumentów\nLista akceptowanych argumentów dostępna pod komendą [-help]")
        return


if __name__ == "__main__":
    main()
