--- Wymagane biblioteki Pythona znajdują się w pliku requirements.txt 
    (instalacja: pip3 install -r requirements.txt)

--- Uruchomienie projektu: python3 main.py [options]

--- Dostępne opcje można wyświetlić korzystając z komendy -help (python3 main.py -help)

--- Program zapisuje grafy w formie graficznej w postaci pliku .png w folderze /images

--- Wagi łuków sieci przepływowej zapisywane są bliżej końca łuku (bliżej strzałki)

---LISTA DOSTĘPNYCH KOMEND:
[-help]              - wyświetla listę dostępnych komend
[-n n]               - liczba warstw pośrednich sieci przepływowej, n >= 2
                       (argument wymagany)
[-fileout1 filename] - plik, do którego ma zostać zapisany obraz losowej sieci 
                       przepływowej (argument opcjonalny)
[-fileout2 filename] - plik, do którego ma zostać zapisany obraz sieci z ustalonym
                       maksymalnym przepływem (argument opcjonalny)

--- Przykładowe wywołania programu:
python3 main.py -n 4 -fileout1 f1 -fileout2 f2
python3 main.py -n 4 -fileout1 f1
python3 main.py -n 4 -fileout2 f2
python3 main.py -n 4

