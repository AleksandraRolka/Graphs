from task02 import randomize_graph

def graf_k_regularny(n, k):

    seq = [ k for i in range(n) ]
    return randomize_graph(100, seq)


if __name__ == "__main__":
    print("Zad 5.")
    print(graf_k_regularny(7, 3))