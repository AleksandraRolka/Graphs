from task01 import *
from task02 import *
from task03 import *

def main():

    graph_input_method = input("\nCzy chcesz wygenerować graf (r), czy wczytać z pliku (p)?\n")

    if graph_input_method == 'r':

        randomize_method = input("\nWybierz metodę losowania grafu: G(n,l) (1), G(n,p) (2)\n")

        if randomize_method == '1':
            randomize_params = input("\nPodaj liczbe wierzchołków n i liczbe krawędzi l\n").split(' ')
            graph_repr = random_with_edges(int(randomize_params[0]), int(randomize_params[1]))

        elif randomize_method == '2':
            randomize_params = input("\nPodaj liczbe wierzchołków n i prawodpodobienstwo wystapienia krawedzi miedzy wierzcholkami p\n").split(' ')
            graph_repr = random_with_probability(int(randomize_params[0]), int(randomize_params[1]))

        else:
            print("Zły argument")
            return

        # jeśli nie udalo się wygenerować grafu to kończymy program
        if graph_repr is None:
            return


    elif graph_input_method == 'p':

        filename = input("\nWskaż nazwę pliku z zapisaną macierzą sąsiedztwa/listą sąsiedztwa/macierzą incydencji:  (np.: input1.txt)\n")

        with open(filename) as f:
            graph_repr = [[int(num) for num in line.split(' ')] for line in f]

    else:
        print("Zły argument")
        return

    
    print("\nNa wejściu:")
    print("---------------------------------------------------")
    print_matrix(graph_repr)
    print()
    repr = reprRecognizer(graph_repr)

    print("\nPozostałe reprezentacje grafu:")
    print("---------------------------------------------------")

    if repr == GraphRepr.ADJ:
        print_matrix(adj2inc(graph_repr))
        print()
        print_matrix(adj2list(graph_repr))
        filename = input("\n\nPodaj nazwę pliku pod jaką chcesz zapisać reprezentację graficzną grafu: (np.: graf)\n")
        filename += '.png'
        draw_graph_from_adj_matrix(graph_repr, filename)
    elif repr == GraphRepr.INC:
        print_matrix(inc2adj(graph_repr))
        print()
        print_matrix(inc2list(graph_repr))
        filename = input("\n\nPodaj nazwę pliku pod jaką chcesz zapisać reprezentację graficzną grafu: (np.: graf)\n")
        filename += '.png'
        draw_graph_from_incid_matrix(graph_repr, filename)
    elif repr == GraphRepr.LIST:
        print_matrix(list2adj(graph_repr))
        print()
        print_matrix(list2inc(graph_repr))
        filename = input("\n\nPodaj nazwę pliku pod jaką chcesz zapisać reprezentację graficzną grafu: (np.: graf)\n")
        filename += '.png'
        draw_graph_from_adj_list(graph_repr,filename)

main()
