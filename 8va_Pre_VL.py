import networkx as nx
#Vladimir Ariel Lizarro Velasquez
Grafo=nx.Graph()
def construir_Grafo(g):
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")
    g.add_node("F")
    g.add_node("G")
    g.add_node("I")
    g.add_edges_from([("A","B"),("A","C"),("A","E"),("A","G"),("A","I")])
    g.add_edges_from([("B","C"),("B","D"),("B","F"),("B","I")])
    g.add_edges_from([("C","D"),("C","E"),("C","G"),("C","I")])
    g.add_edges_from([("D","E"),("D","G"),("D","I")])
    g.add_edges_from([("E","F"),("E","G"),("E","I")])
    g.add_edges_from([("F","G")])
    g.add_edges_from([("G","I")])
def matriz_Adyacencia(g):
    m=nx.adjacency_matrix(g)
    print(m.todense())
def comb_Tod_Cam(g):
    v=set()
    for nod_In in g.nodes():
        for nod_Fi in g.nodes():
            if (nod_In != nod_Fi):
                for camino in nx.all_simple_paths(g, source=nod_In, target=nod_Fi):
                    camino_tupla=tuple(sorted(camino))
                    v.add(camino_tupla)
    for i, j in enumerate(v):
        print(f"Camino {i+1}: {j}")
if __name__ == '__main__':
    construir_Grafo(Grafo)
    comb_Tod_Cam(Grafo)
