# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:22:49 2025

@author: jveraz
"""

######################################################
# Mini Proyecto 2: Diccionario Literario Interactivo #
######################################################

# Crear un diccionario de autores y sus obras
autores = {
    "Cervantes": "Don Quijote de la Mancha",
    "Borges": "Ficciones",
    "García Márquez": "Cien años de soledad",
    "Cortázar": "Rayuela"
}

# Función para buscar una obra por autor
def buscar_obra(autor):
    return autores.get(autor, "No tengo información de ese autor.")

# Interacción con el usuario
autor = input("Escribe el nombre de un autor para conocer su obra más famosa: ")
print(f"{autor}: {buscar_obra(autor)}")
