# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:27:37 2025

@author: jveraz
"""

#####################################
# Parámetros y Retorno de Funciones #
#####################################

# Función para contar palabras en un texto sin usar split()
def contar_palabras(texto):
    contador = sum(1 for letra in texto if letra == " ") + 1
    return contador

# Uso de la función
texto = "Python es muy útil para analizar literatura."
print("El texto tiene " + str(contar_palabras(texto)) + " palabras.")

# Función con múltiples parámetros
def detalles_libro(titulo, autor, año):
    return "El libro " + titulo + " fue escrito por " + autor + " en el año " + str(año) + "."

print(detalles_libro("Rayuela", "Julio Cortázar", 1963))
