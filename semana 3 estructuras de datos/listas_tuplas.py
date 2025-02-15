# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:20:57 2025

@author: jveraz
"""

#############################
# Listas y Tuplas en Python #
#############################

# LISTAS: Colecciones ordenadas y modificables
autores = ["Borges", "Cortázar", "García Márquez", "Vargas Llosa"]
print("Lista de autores:", autores)

# Acceder a elementos
print("Primer autor:", autores[0])

# Modificar listas sin usar append()
autores = autores + ["Shakespeare"]  # Agregar nuevo autor
autores = autores[:2] + ["Cervantes"] + autores[2:]  # Insertar en posición específica
print("Lista modificada:", autores)

# Crear lista vacía e ir agregando elementos
poetas = []
poetas = poetas + ["Neruda"]
poetas = poetas + ["Vallejo"]
print("Poetas:", poetas)

# TUPLAS: Colecciones ordenadas e inmutables
generos = ("Poesía", "Novela", "Ensayo", "Teatro")
print("Géneros literarios:", generos)

# Intentar modificar una tupla (esto fallará)
# generos[0] = "Cuento"  # Descomentar para ver error
