--- Wymagane biblioteki Pythona znajdują się w pliku requirements.txt 
    (instalacja: pip3 install -r requirements.txt)

--- Uruchomienie projektu: python3 main.py [options]

--- Dostępne opcje można wyświetlić korzystając z komendy -help (python3 main.py -help)

--- Użytkownik podaje graf wejściowy w formie pliku .txt (folder graph_representations)
    (przykładowe pliki: input1.txt, input2.txt, input3.txt, input4.txt - kolejno macierz sąsiedztwa, lista sąsiedztwa, macierz incydencji, macierz, którą można interpretować dwojako)

--- Program zapisuje grafy w formie graficznej w postaci pliku .png

--- Przykładowe wywołania programu:
python main.py -random_coherent_weighted_graph -n 8 -out test1
python main.py -random_coherent_weighted_graph -n 8 -a 3 -b 11 -out test2
python main.py -dijkstra -graph input.txt -out test3
python main.py -distance_matrix -n 8 -out test4
python main.py -graph_centers -n 8 -out test5
python main.py -minimal_spanning_tree -n 8 -out test6
