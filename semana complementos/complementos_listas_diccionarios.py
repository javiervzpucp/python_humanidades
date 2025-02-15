# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:49:06 2025

@author: jveraz
"""

#########################################
# Complementos de Listas y Diccionarios #
#########################################

# Comprensión de listas
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print("Cuadrados:", cuadrados)

# Diccionarios anidados
autores = {
    "Cervantes": {"Obra": "Don Quijote", "Siglo": "XVII"},
    "Borges": {"Obra": "Ficciones", "Siglo": "XX"},
}

# Iterar sobre diccionarios anidados
for autor, info in autores.items():
    print(f"{autor} escribió {info['Obra']} en el siglo {info['Siglo']}.")

# Uso de zip() para unir listas
nombres = ["Julio", "Gabriel", "Mario"]
obras = ["Rayuela", "Cien años de soledad", "Conversación en la catedral"]
parejas = list(zip(nombres, obras))
print("Autores y obras:", parejas)

# Uso de enumerate() para numerar elementos
for indice, nombre in enumerate(nombres, start=1):
    print(f"{indice}. {nombre}")
