# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:34:30 2025

@author: jveraz
"""

##############################################
# Análisis de Datos en Humanidades Digitales #
##############################################

import pandas as pd

# Cargar datos de autores y obras desde CSV
df = pd.read_csv("autores.csv", encoding="utf-8")

# Filtrar autores después del año 1900
df_moderno = df[df["Año"] > 1900]

print("Autores modernos:")
print(df_moderno)

# Contar cuántos libros hay por siglo
df["Siglo"] = df["Año"] // 100 + 1
conteo_siglo = df["Siglo"].value_counts()

print("\nNúmero de libros por siglo:")
print(conteo_siglo)
