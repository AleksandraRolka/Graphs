from utils import *
import random as rnd



def set_random_weight(adj_matrix, a, b):

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                adj_matrix[i][j] = rnd.randint(a, b)
                
    return adj_matrix


def generate_random_coherent_weighted_graph(n,a = 1,b = 10):
    '''
        
    '''
        
    seq = gen_random_seq(n)
    graph = seq_to_adj_matrix(seq) 
    graph = rearange_matrix_by_seq(graph, seq)

    while not only_one_comp(graph):
        seq = gen_random_seq(n)
        graph = seq_to_adj_matrix(seq)
        graph = rearange_matrix_by_seq(graph, seq)
    
    graph = set_random_weight(graph,a,b)
    
    return graph

if __name__ == "__main__":
    
    n = 0
    n = int(input("\nPodaj liczbę n:\n"))

    graph = generate_random_coherent_weighted_graph(n)
    
    print_matrix(graph)
    draw_graph_from_adj_matrix(graph,'graf1')
    
    