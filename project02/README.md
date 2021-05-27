### Instalacja wymaganych bibliotek przed uruchomieniem programu:

```
pip3 install -r requirements.txt
```

### Wywołanie programu `python3 main.py` z odpowiednimi flagami:

LISTA DOSTĘPNYCH KOMEND:

- [```-help```] - wyświetla listę dostępnych komend
- [```-is_graphic_seq```] - sprawdza czy sekwencja jest ciągiem graficznym
- [```-randomize_graph```] - randomizuje [n] razy graf prosty
- [```-largest_connected_component```] - znajduje największą spójną składową graf
- [```-random_eulerian_graph```] - generuje losowy graf Eulera i znajduje w nim cykl Eulera
- [```-random_k_regular_graph```] - generuje losowy graf k-regularny
- [```-is_hamiltonian_graph```] - sprawdza czy graf jest hamiltonowski, jeśli tak to zwraca cykl Hamiltona

** Aby sprawdzić z jakimi argumentami wywołuje się dany program uruchom z `-help`, np. `python3 main.py -is_graphic_seq -help` **
<br/>** Aby zapisać graficzną reprezentacje wynikowego grafu \_**:
[-fileout filename] - [filename] nazwa pliku, do którego ma zostać zapisany obraz grafu w formacie png
<br/><br/><br/>

POCZSZEGÓLNE PODKOMENDY:

- PODKOMENDY DO `-is_graphic_seq`:
  - [```-seq seq```] - sprawdza czy podana na wejściu sekwencja [seq] (separator=' ') jest ciągiem graficznym
  - [```-filein filename```] - sprawdza czy sekwencja z pliku graph_representations/[filename] jest ciągiem graficznym
- `-randomize_graph`:
  - [```-seq seq -n n```] - randomizuje [n] razy graf prosty o zadanym ciągu [seq] stopni wierzchołków
  - [```-filein filename -n n```] - randomizuje [n] razy graf prosty o zadanym ciągu stopni wierzchołków, z pliku graph_representations/[filename]
- `-largest_connected_component`:
  - [```-filein filename```] - znajduje największą spójną składową grafu, znajdującego się w pliku graph_representations/[filename]
    (możliwe postacie wejściowego grafu: macierz sąsiedztwa, macierz incydencji, lista sąsiedztwa, ciąg)
  - [```-gnl -n n -l l```] - znajduje największą spójną składową wygenerowanego losowego grafu o [n] wierzchołkach i [l] krawędziach
  - [```-gnp -n n -p p```] - znajduje największą spójną składową wygenerowanego losowego grafu o [n] wierzchołkach i [p] prawdop. wystąpienia krawędzi,
- `-random_eulerian_graph`:
  - [```-n n```] - generuje losowy graf Eulera o [n] wierzchołkach i znajduje w nim cykl Eulera
- `-random_k_regular_graph`:
  - [```-n n -k k```] - generuje losowy graf [k]-regularny o [n] wierzchołkach
- `-is_hamiltonian_graph`:
  - [```-filein filename```] - sprawdza czy graf (postać:lista sąsiedztwa) znajdujący się w pliku jest hamiltonowski, jeśli tak to zwraca cykl Hamiltona
