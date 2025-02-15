# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:48:09 2025

@author: jveraz
"""

#############################
# Lógica Avanzada en Python #
#############################

# Expresiones lógicas más complejas
a = 5
b = 10
c = 15

resultado = (a < b and b < c) or not (a == 5)
print("Resultado de la expresión lógica:", resultado)

# Uso de operadores de comparación
print("¿b es mayor que a y menor que c?", a < b < c)

# Comprobaciones con valores nulos y booleanos
valor = None
if valor is None:
    print("La variable no tiene un valor asignado.")
