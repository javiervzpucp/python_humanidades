# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:49 2025

@author: jveraz
"""

###############################################################
# Proyecto: Análisis de Datos en Humanidades con Scikit-Learn #
###############################################################

# REQUISITOS: Instalar scikit-learn antes de ejecutar
# pip install scikit-learn

from sklearn.feature_extraction.text import CountVectorizer

# Lista de textos históricos
textos = [
    "Don Quijote cabalgó por los campos de La Mancha.",
    "Sancho Panza fue su fiel escudero en la aventura.",
    "La locura del caballero era legendaria."
]

# Vectorizar los textos para analizar su frecuencia de palabras
vectorizador = CountVectorizer()
matriz = vectorizador.fit_transform(textos)

# Mostrar la matriz de palabras
print("Palabras analizadas:", vectorizador.get_feature_names_out())
print(matriz.toarray())
