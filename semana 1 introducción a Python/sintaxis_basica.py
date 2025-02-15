# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:10:33 2025

@author: jveraz
"""

#############################
# Sintaxis Básica de Python #
#############################

# Tipos de datos básicos en Python
entero = 42
flotante = 3.14
cadena = "Python para humanistas"
booleano = True

print(type(entero), type(flotante), type(cadena), type(booleano))

# Uso de condicionales básicos
edad = int(input("Introduce tu edad: "))

if edad > 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

