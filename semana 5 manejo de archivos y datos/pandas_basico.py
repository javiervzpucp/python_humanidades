# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:33:59 2025

@author: jveraz
"""

####################################################
# Introducción a Pandas para Humanidades Digitales #
####################################################

import pandas as pd

# Crear un DataFrame manualmente
datos = {
    "Autor": ["Cervantes", "García Márquez", "Cortázar", "Neruda"],
    "Obra": ["Don Quijote", "Cien años de soledad", "Rayuela", "Veinte poemas"],
    "Año": [1605, 1967, 1963, 1924]
}

df = pd.DataFrame(datos)

print("Tabla de autores y obras:")
print(df)

# Guardar en CSV
df.to_csv("autores.csv", index=False, encoding="utf-8")

# Leer desde un CSV
df_leido = pd.read_csv("autores.csv", encoding="utf-8")
print("\nDatos leídos desde CSV:")
print(df_leido)
