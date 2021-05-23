from task02 import *
import sys


def main():
    args = sys.argv[1:]
    alen = len(args)

    filename_out1 = None
    filename_out2 = None
    n = None

    # Parsowanie podanych argumentów wywołania programu
    if alen > 0:
        try:
            if "-help" in args:
                print("""
-----------------------------------------------------------------------------------
Lista dostępnych komend:
[-help]              - wyświetla listę dostępnych komend
[-n n]               - liczba warstw pośrednich sieci przepływowej, n >= 2
                      (argument wymagany)
[-fileout1 filename] - plik, do którego ma zostać zapisany obraz losowej sieci 
                       przepływowej (argument opcjonalny)
[-fileout2 filename] - plik, do którego ma zostać zapisany obraz sieci z ustalonym
                       maksymalnym przepływem (argument opcjonalny)

Przykład wywołania programu:
python3 main.py -n 4 -fileout1 f1 -fileout2 f2
-----------------------------------------------------------------------------------
                """)
                return

            if "-fileout1" in args:
                idx = args.index("-fileout1")
                filename_out1 = args[idx+1]
            if "-fileout2" in args:
                idx = args.index("-fileout2")
                filename_out2 = args[idx+1]

            if "-n" in args:
                idx = args.index("-n")
                n = int(args[idx+1])
            else:
                print("Nie podano liczby warstw sieci przepływowej")
                return
            if n < 2:
                print(
                    "Ilość warstw pośrednich sieci przepływowej musi być większa lub równa 2 (podano: ", n, ")", sep='')
                return

        except IndexError:
            print(
                "Podano nieprawidłową ilość argumentów\nIlość oczekiwanych argumentów dla każdej z flag można znaleźć korzystając z flagi [-help]")
            return
        except ValueError as e:
            err_str = e.args[0]
            value_idx = err_str.find("'")
            print("Wartość n musi być liczbą całkowitą (podano ",
                  err_str[value_idx:], ")", sep='')
            return
        except Exception as e:
            print(e)
            return

        print("Tworzenie losowej sieci przepływowej...")
        g, layers = random_network(n)
        if filename_out1 == None:
            print("\nMacierz sąsiedztwa wylosowanej sieci:")
            print_matrix(g)
        else:
            draw_graph_from_adj_matrix(
                g, layers, fname=filename_out1, with_weights=True)
            print("Obraz losowej sieci przepływowej zapisano w pliku: images/",
                  filename_out1, sep='')

        print("\nObliczanie maksymalnego przepływu dla wylosowanej sieci...")
        f, fmax = ford_fulkerson(g)
        print("Wartość maksymalnego przepływu: fmax =", fmax)
        if filename_out2 != None:
            draw_graph_from_adj_matrix(
                g, layers, flow=f, fname=filename_out2, with_weights=True)
            print("Obraz sieci z ustalonym maksymalnym przepływem zapisano w pliku: images/",
                  filename_out2, sep='')

    else:
        print(
            "Nie podano żadnych argumentów\nLista akceptowanych argumentów dostępna pod komendą [-help]")
        return


if __name__ == "__main__":
    main()
