# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:29:34 2025

@author: jveraz
"""

####################################
# Evaluación Automática con Pytest #
####################################
# Este archivo permite verificar si los ejercicios de la tarea han sido resueltos correctamente.
# Para ejecutar las pruebas:
# 1️Instalar pytest si no está instalado:
#    pip install pytest
# Guardar las funciones en `tareas.py` (o el nombre correcto del archivo donde estén)
# Ejecutar pytest desde la terminal:
#    pytest test_tareas.py
# Si el código está correcto, todas las pruebas pasarán.

# 🔹 Importamos las funciones de la tarea
from tareas import contar_palabras

# 🔹 Evaluamos la función contar_palabras
def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("Python para Humanidades Digitales") == 4
    assert contar_palabras("") == 0
