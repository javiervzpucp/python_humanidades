# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:39:18 2025

@author: jveraz
"""

##################################################
# Introducción a la Visualización con Matplotlib #
##################################################

import matplotlib.pyplot as plt

# Datos de libros publicados por autor
autores = ["Cervantes", "García Márquez", "Cortázar", "Borges"]
libros = [3, 5, 4, 6]

# Crear gráfico de barras
plt.bar(autores, libros, color="blue")
plt.xlabel("Autores")
plt.ylabel("Cantidad de libros publicados")
plt.title("Cantidad de libros por autor")
plt.show()
