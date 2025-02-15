# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:28:59 2025

@author: jveraz
"""

##########################
# Programación Funcional en Python
##########################

# Uso de funciones lambda para transformar textos
capitalizar = lambda texto: texto.title()

texto = "miguel de cervantes escribió don quijote"
print(capitalizar(texto))

# Función que recibe otra función como argumento
def aplicar_funcion(func, texto):
    return func(texto)

print(aplicar_funcion(capitalizar, "borges y la literatura fantástica"))

# Uso de map() para transformar una lista de textos
autores = ["borges", "cortázar", "garcía márquez"]
autores_capitalizados = list(map(capitalizar, autores))

print("Autores:", autores_capitalizados)
