# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:36:00 2025

@author: jveraz
"""

###############################################
# Expresiones Regulares para Análisis Textual #
###############################################

import re

# Texto de ejemplo: fragmento de un poema
texto = "Verde que te quiero verde. Verde viento. Verdes ramas."

# Buscar todas las palabras que comiencen con "Verde"
patron = r"\bVerde\b"
resultados = re.findall(patron, texto)

print("Palabras encontradas:", resultados)

# Reemplazar "Verde" por "Azul"
texto_modificado = re.sub(patron, "Azul", texto)
print("Texto modificado:", texto_modificado)

# Extraer todas las palabras del texto
palabras = re.findall(r"\b\w+\b", texto)
print("Lista de palabras:", palabras)

# Encontrar palabras con más de 5 letras
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print("Palabras largas:", palabras_largas)
