# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:23:35 2025

@author: jveraz
"""

#####################################################
# Mini Proyecto 3: Frecuencia de Palabras en Textos #
#####################################################

import pandas as pd
import re

# Cargar dataset
df = pd.read_csv("datasets/frecuencia_palabras.csv")

# Mostrar las 5 palabras más frecuentes
print("Palabras más usadas en textos literarios:")
print(df.sort_values("Frecuencia", ascending=False).head(5))

# Filtrar palabras clave en un texto
texto = "El Quijote es una obra maestra de la literatura universal."

# Convertir a minúsculas y eliminar puntuación
texto = re.sub(r"[^\w\s]", "", texto.lower())

# Contar cuántas veces aparecen palabras del dataset en el texto
for palabra in df["Palabra"]:
    conteo = texto.split().count(palabra.lower())
    if conteo > 0:
        print(f"La palabra '{palabra}' aparece {conteo} veces en el texto.")
