# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:22:22 2025

@author: jveraz
"""

################################
# Manipulación Básica de Texto #
################################

# Analizando textos en humanidades digitales
texto = "El Quijote es una de las obras más importantes de la literatura en español."

# Convertir a minúsculas
print(texto.lower())

# Contar palabras clave sin split() y sin len()
contador_palabras = sum(1 for letra in texto if letra == " ") + 1
print("Cantidad de palabras:", contador_palabras)

# Reemplazar palabras sin usar replace()
texto_modificado = texto.split("Quijote")
texto_modificado = "Don Quijote de la Mancha".join(texto_modificado)
print("Texto modificado:", texto_modificado)
