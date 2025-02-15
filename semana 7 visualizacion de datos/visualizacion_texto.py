# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:39:55 2025

@author: jveraz
"""

#######################################################
# Visualización de Frecuencia de Palabras en un Texto #
#######################################################

import matplotlib.pyplot as plt
from collections import Counter

# Texto de ejemplo
texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme..."

# Convertir a minúsculas y eliminar puntuación
texto = texto.lower().replace(",", "").replace(".", "")

# Contar frecuencia de palabras
palabras = texto.split()
frecuencia = Counter(palabras)

# Obtener las 5 palabras más frecuentes
top_palabras = frecuencia.most_common(5)

# Graficar
palabras, conteo = zip(*top_palabras)
plt.bar(palabras, conteo, color="green")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.title("Palabras más frecuentes en el texto")
plt.show()
