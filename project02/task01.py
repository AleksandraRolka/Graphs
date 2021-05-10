import copy


def degree_seq(A, n):
    """
        Funkcja sprawdza czy dany ciag liczb jest ciagiem graficznym
        A - ciag liczb naturalnych
        n - liczba elementow w ciagu liczb
    """
    # sortujemy ciag nierosnaco
    A_s = sorted(A, reverse=True)
    # jesli ilosc nieparzystych elementow ciagu jest nieparzysta ciag nie jest graficzny
    if (sum(i % 2 for i in A_s)) % 2:
        return False
    while True:
        if all(el == 0 for el in A_s):
            return True
        elif A_s[0] < 0 or A_s[0] >= n or all(el < 0 for el in A_s[1:]):
            return False
        else:
            for i in range(1, A_s[0] + 1):
                if A_s[i] >= 1:
                    A_s[i] = A_s[i] - 1
                else:
                    return False
            A_s[0] = 0
            A_s.sort(reverse=True)

# ----------------------------------------------------------------------------------


def seq_to_adj_matrix(seq):
    """
        Funkcja tworzy macierz sasiedztwa na podstawie ciagu liczb
        seq - ciag liczb naturalnych
    """
    if degree_seq(seq, len(seq)) == False:
        print("Dana sekwencja liczb nie jest ciagiem graficznym!")
        return
    size = len(seq)
    seqSorted = copy.copy(seq)
    seqSorted.sort(reverse=True)

    # tworzymy liste par [numer wierzchołka-stopien]
    my_list = [[i, seqSorted[i]] for i in range(0, size)]
    # tworzymy zerowa macierz sasiadujaca nxn
    adj_matrix = [[0 for i in range(size)] for j in range(size)]

    for i in range(0, size):
        # sortujemy liste po stopniu
        my_list = sorted(my_list, key=lambda x: x[1], reverse=True)
        # od następnych par aktualego elementu listy odejmujemy 1 - tworzymy krawedz
        # oraz uaktualniamy macierz sasiedztwa
        for el in my_list[1: my_list[0][1]+1]:
            adj_matrix[my_list[0][0]][el[0]] = 1
            adj_matrix[el[0]][my_list[0][0]] = 1
            el[1] -= 1
        # aktualny element ma teraz odpowiednia liczbe krawedzi wychodzacych z niego - usuwamy go z listy
        my_list.pop(0)
        # sortujemy na nowo uaktualniona liste
        my_list = sorted(my_list, key=lambda x: x[1], reverse=True)

    return adj_matrix
