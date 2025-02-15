# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:21:30 2025

@author: jveraz
"""

##########################
# Diccionarios en Python #
##########################

# Un diccionario almacena información con pares clave-valor.
libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}

# Acceder a valores
print(f"El libro {libro['titulo']} fue escrito por {libro['autor']} en {libro['año']}.")

# Agregar un nuevo dato sin usar update()
libro["género"] = "Realismo mágico"
libro = {**libro, "idioma": "Español"}  # Otra forma de agregar datos sin update()
print("Libro actualizado:", libro)

# Iterar sobre diccionarios
for clave, valor in libro.items():
    print(f"{clave}: {valor}")
