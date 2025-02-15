# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:24:04 2025

@author: jveraz
"""

#################################################### 
# Mini Proyecto 4: Análisis de Discursos Políticos #
####################################################

import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("datasets/discursos_historicos.csv")

# Contar cuántas veces aparecen palabras clave en los discursos
conteo_palabras = df["Palabras_Clave"].str.split(",").explode().value_counts()

# Graficar los resultados
plt.bar(conteo_palabras.index, conteo_palabras.values, color="red")
plt.xlabel("Palabras Clave")
plt.ylabel("Frecuencia en los Discursos")
plt.title("Palabras más usadas en Discursos Históricos")
plt.xticks(rotation=45)
plt.show()
