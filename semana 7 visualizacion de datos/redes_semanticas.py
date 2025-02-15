# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:40:21 2025

@author: jveraz
"""

##############################################
# Construcción de Redes Semánticas en Python #
##############################################

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.Graph()

# Agregar nodos (palabras clave)
G.add_nodes_from(["literatura", "poesía", "novela", "ensayo", "cuento"])

# Agregar relaciones entre palabras
G.add_edges_from([
    ("literatura", "poesía"),
    ("literatura", "novela"),
    ("literatura", "ensayo"),
    ("novela", "cuento"),
])

# Dibujar la red semántica
plt.figure(figsize=(5, 5))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=12)
plt.title("Red Semántica de Géneros Literarios")
plt.show()
