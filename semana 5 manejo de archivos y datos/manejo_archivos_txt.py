# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:33:12 2025

@author: jveraz
"""

#########################################
# Manejo de Archivos de Texto en Python #
#########################################

# Escribir en un archivo
with open("literatura.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Don Quijote de la Mancha - Miguel de Cervantes\n")
    archivo.write("Cien años de soledad - Gabriel García Márquez\n")

# Leer un archivo
with open("literatura.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)

# Agregar más líneas sin sobrescribir el archivo
with open("literatura.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Rayuela - Julio Cortázar\n")

# Leer línea por línea
with open("literatura.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print("Línea:", linea.strip())
