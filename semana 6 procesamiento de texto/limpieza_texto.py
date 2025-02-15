# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:36:37 2025

@author: jveraz
"""

#########################################
# Limpieza de Texto en Análisis Digital #
#########################################

import re

# Texto con símbolos, mayúsculas y espacios innecesarios
texto = "¡Hola! Me llamo Miguel de Cervantes. ¿Cómo estás?"

# Convertir a minúsculas
texto = texto.lower()

# Eliminar signos de puntuación
texto = re.sub(r"[^\w\s]", "", texto)

# Eliminar múltiples espacios
texto = re.sub(r"\s+", " ", texto).strip()

print("Texto limpio:", texto)
