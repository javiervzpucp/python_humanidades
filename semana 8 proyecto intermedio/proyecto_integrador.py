# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:42:15 2025

@author: jveraz
"""

######################################################
# Proyecto Integrador: Análisis de Textos Literarios #
######################################################

import re
from collections import Counter
import matplotlib.pyplot as plt

# Función para limpiar texto
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", "", texto)  # Eliminar puntuación
    return texto

# Cargar y limpiar el texto
with open("texto_literario.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

texto_limpio = limpiar_texto(texto)

# Contar frecuencia de palabras
palabras = texto_limpio.split()
frecuencia = Counter(palabras)

# Obtener las 10 palabras más comunes
top_palabras = frecuencia.most_common(10)

# Graficar
palabras, conteo = zip(*top_palabras)
plt.bar(palabras, conteo, color="purple")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.title("Palabras más frecuentes en el texto literario")
plt.xticks(rotation=45)
plt.show()
