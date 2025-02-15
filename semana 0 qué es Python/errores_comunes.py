# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:46:02 2025

@author: jveraz
"""

################################################
# Errores Comunes en Python y Cómo Resolverlos #
################################################

# 1. Error de sintaxis (SyntaxError)
#    print("Hola, mundo"  # Falta cerrar el paréntesis
#    Solución: Asegurarse de escribir correctamente la sintaxis.

# 2. Nombre no definido (NameError)
#    print(variable_no_definida)  # Variable no existe
#    Solución: Definir la variable antes de usarla.

# 3. Error de tipo (TypeError)
#    resultado = "10" + 5  # No se puede sumar string con número
#    Solución: Convertir tipos antes de operar: int("10") + 5

# 4. Índice fuera de rango (IndexError)
#    lista = ["A", "B", "C"]
#    print(lista[5])  # No existe el índice 5
#    Solución: Verificar el tamaño de la lista antes de acceder a un índice.

print("Ejemplo sin errores:")
print("Python es fácil de aprender.")
