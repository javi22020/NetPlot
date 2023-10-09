import pydot as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

lista_neuronas = [12, 16, 16, 4]

lista_pesos = []
for i in range(len(lista_neuronas) - 1):
    lista_pesos.append(np.random.randn(lista_neuronas[i + 1], lista_neuronas[i]))

def crear_grafo(lista_neuronas: list, lista_pesos: list):
    red = pd.Dot("Red", graph_type='digraph')
    red.set_graph_defaults(rankdir="LR", lwidth=50)
    for num_capa in range(len(lista_neuronas)):
        s_grafo = pd.Subgraph(graph_name="Capa" + str(num_capa))
        for neurona in range(lista_neuronas[num_capa]):
            nodo = pd.Node(name="C" + str(num_capa) + "N" + str(neurona))
            s_grafo.add_node(nodo)
        red.add_subgraph(s_grafo)
    
    lista_subgrafos = red.get_subgraph_list()
    for num_capa_subgrafo in range(len(lista_subgrafos) - 1): # Bucle para crear aristas entre capas
        capa_actual = lista_subgrafos[num_capa_subgrafo].get_node_list()
        capa_siguiente = lista_subgrafos[num_capa_subgrafo + 1].get_node_list()
        for neurona_actual in range(len(capa_actual)):
            for neurona_siguiente in range(len(capa_siguiente)):
                red.add_edge(pd.Edge(capa_actual[neurona_actual], capa_siguiente[neurona_siguiente], label=str(round(lista_pesos[num_capa_subgrafo][neurona_siguiente][neurona_actual], 3))))

    print("Se han guardado " + str(len(red.get_subgraph_list())) + " subgrafos y " + str(len(red.get_edge_list())) + " aristas. ")
    return red

# dibujar_grafo(posiciones(lista_neuronas=lista_neuronas, x=1080, y=1080, radio=25))
red_dot = crear_grafo(lista_neuronas=lista_neuronas, lista_pesos=lista_pesos)

open("temp.gv", "w").write(str(red_dot))

red_dot.write_png("output.png")
