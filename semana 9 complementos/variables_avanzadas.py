# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:48:40 2025

@author: jveraz
"""

#################################
# Variables Avanzadas en Python #
#################################

# Mutabilidad e inmutabilidad
numero = 10  # Inmutable (enteros)
texto = "Python"  # Inmutable (cadenas)
lista = [1, 2, 3]  # Mutable

# Modificar una lista sin afectar la variable original
nueva_lista = lista + [4, 5]
print("Lista original:", lista)
print("Lista modificada:", nueva_lista)

# Variables locales y globales
def ejemplo_variable():
    local = "Soy una variable local"
    print(local)

ejemplo_variable()

global_var = "Soy global"

def modificar_global():
    global global_var
    global_var = "Cambié la variable global"

modificar_global()
print(global_var)
