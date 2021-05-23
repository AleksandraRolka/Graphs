from task01 import *
import math


def cf(u, v, G, c, f):
    """
        Funkcja zwracająca przepustowość
        rezydualną krawędzi (u, v)
    """
    if G[u][v] != 0:
        return c[(u, v)] - f[(u, v)]
    if G[v][u] != 0:
        return f[(v, u)]
    return 0


def bfs(G, s, t):
    """
        Przeszukiwanie wszerz\n
        G - macierz sąsiedztwa\n
        s - wierzchołek startowy
    """
    if s >= len(G) or s < 0:
        print("Podano niepoprawny numer wierzchołka startowego")
        exit()
    if t >= len(G) or t < 0:
        print("Podano niepoprawny numer wierzchołka końcowego")
        exit()
    d = [math.inf for _ in range(len(G))]
    p = [None for _ in range(len(G))]
    d[s] = 0

    Q = []
    Q.append(s)

    while len(Q) > 0 and d[t] == math.inf:
        v = Q.pop(0)
        for u in range(len(G)):
            if G[v][u] != 0:
                if d[u] == math.inf:
                    d[u] = d[v] + 1
                    p[u] = v
                    Q.append(u)
            if d[t] != math.inf:
                break
    return d, p


def ford_fulkerson(G):
    """
        Algorytm Forda-Fulkersona\n
        G - macierz sąsiedztwa
    """
    s = 0
    t = len(G)-1

    f = {}
    c = {}
    # Zerowanie przepływów i ustalanie przepustowości poszczególnych krawędzi
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v] != 0:
                f[(u, v)] = 0
                c[(u, v)] = G[u][v]

    # Tworzenie sieci rezydualnej Gf (aktualizacja co każdą iterację)
    Gf = [[cf(u, v, G, c, f) for v in range(len(G))] for u in range(len(G))]
    (d, p) = bfs(Gf, s, t)

    while d[t] != math.inf:
        # Dodawanie krawędzi do ścieżki rozszerzającej
        path = []
        v = t
        while v != None and p[v] != None:
            path.append((p[v], v))
            v = p[v]
        path.reverse()

        # Wyznaczanie cf(p)
        cf_p = math.inf
        for i in range(len(path)):
            u = path[i][0]
            v = path[i][1]
            _cf = cf(u, v, G, c, f)
            if _cf < cf_p:
                cf_p = _cf

        for i in range(len(path)):
            u = path[i][0]
            v = path[i][1]
            if G[u][v] != 0:
                f[(u, v)] += cf_p
            else:
                f[(v, u)] -= cf_p

        Gf = [[cf(u, v, G, c, f) for v in range(len(G))]
              for u in range(len(G))]
        (d, p) = bfs(Gf, s, t)

    # Obliczanie wartości maksymalnego przepływu fmax
    fmax = 0
    keys = list(f.keys())
    values = list(f.values())
    for i in range(len(f)):
        if 0 in keys[i]:
            fmax += values[i]

    return f, fmax


if __name__ == "__main__":
    pass
