--- Wymagane biblioteki Pythona znajdują się w pliku requirements.txt 
    (instalacja: pip3 install -r requirements.txt)

--- Uruchomienie projektu: python3 main.py [options]

--- Dostępne opcje można wyświetlić korzystając z komendy help (python3 main.py help)

--- W przypadku opcji kosaraju dla wczytanego pliku -filein graf musi być zapisany w postaci macierzy sąsiedztwa

--- Program zapisuje grafy w formie graficznej w postaci pliku .png

--- W przypadku łuków w obie strony - waga jest zapisana na łuku bliżej jego końca, czyli wbliżej wierzchołka docelowego 

---LISTA DOSTĘPNYCH KOMEND:
[help]                                         - wyświetla listę dostępnych komend
[random_digraph_with_probability]              - generuje losowy graf skierowany
[kosaraju]                                     - algorytm kosaraju - zwraca silnie spójne składowe digrafu wraz z wypisaniej tej największej
[bellmann_ford]                                - algorytm Bellmanna-Forda - zwraca macierz odległości
[johnson]                                      - algorytm Johnsona - zwraca macierz odległości

*** Aby sprawdzić z jakimi argumentami wywołuje się dany program uruchom z "-help", np. "python3 main.py kosaraju -help" ***
*** Aby zapisać graficzną reprezentacje wynikowego grafu:
[-fileout filename]                             - [filename] nazwa pliku, do którego ma zostać zapisany obraz grafu w formacie png


---Poszczególne opcje wywołania:
*dla [random_digraph_with_probability]:
(-n n -p p) || [-fileout filename]       	- generuje losowy graf skierowany o [n] wierzchołkach i [p] prawdopodobieństwie wystąpienia krawędzi
                                           	opcja dodatkowa -fileout - zapisze graf do pliku [filename] w folderze graph_examples
*dla [kosaraju]:
(-n n -p p) || [-fileout filename]              - zwraca silnie spójne skladowe dla losowego grafu skierowanego o [n] wierzchołkach i [p] prawdopodobieństwie wystąpienia krawędzi
(-filein filename) || [-fileout filename]       - zwróci silnie spójne składowe dla grafu zapisanego w pliku [filename] w folderze graphs_examples 
                                                  (graf w pliku powinien być w postaci macierzy sąsiedztwa) 
                                                - dodatkowa opcja -fileout zapisze graf do pliku [filename] w folderze graph_examples
*dla [bellmann_ford]:
(-n n -p p -a a -b b) || [-fileout filename]    - znajduje najkrótsze ścieżki dla losowego grafu skierowanego o [n] wierzchołkach 
                                                  i [p] prawdopodobieństwie wystąpienia krawędzi o losowych wagach z przedziału [a, b]
(-default) || [-fileout filename]               - znajduje najkrótsze ścieżki dla losowego grafu skierowanego o domyślnych parametrach: [n = 6] wierzchołkach i [p = 0.3] prawdopodobieństwie
                                                  wystąpienia krawędzi o losowych wagach z przedziału [a = -5, b = 10]
                                                - opcja dodatkowa -fileout zapisze graf do pliku [filename] w folderze graph_examples

*dla [johnson]:
(-n n -p p -a a -b b) || [-fileout filename]    - znajduje najkrótsze ścieżki między parami wierzchołków dla losowego grafu skierowanego o [n] wierzchołkach 
                                                  i [p] prawdopodobieństwie wystąpienia krawędzi o losowych wagach z przedziału [a, b]
(-default) || [-fileout filename]               - znajduje najkrótsze ścieżki dla losowego grafu skierowanego o domyślnych parametrach: [n = 6] wierzchołkach
                                                  i [p = 0.3] prawdopodobieństwie wystąpienia krawędzi o losowych wagach z przedziału [a = -5, b = 10]
                                                - dodatkowa opcja -fileout zapisze graf do pliku [filename] w folderze graph_examples


--- Przykładowe wywołania programu:
python3 main.py random_digraph_with_probability -n 10 -p 0.1 -fileout test1
python3 main.py kosaraju -n 10 -p 0.2 -fileout test2
python3 main.py kosaraju -filein graph.txt -fileout test3
python3 main.py bellmann_ford -n 8 -p 0.1 -a -5 -b 15 -fileout test4
python3 main.py bellmann_ford -default -fileout test5
python3 main.py johnson -n 10 -p 0.2 -a -10 -b 10 -fielout test6
python3 main.py johnson -default -fileout test7


