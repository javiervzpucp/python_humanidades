# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:57:17 2025

@author: jveraz
"""

########################################################
# Proyecto: Uso de APIs de IA en Humanidades Digitales #
########################################################

# REQUISITOS: Instalar requests antes de ejecutar
# pip install requests

import requests

# API de IA para generación de texto (ejemplo con Hugging Face)
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HEADERS = {"Authorization": "Bearer TU_CLAVE_DE_API"}

# Texto para resumen automático
texto = "Don Quijote es una obra maestra de la literatura española escrita por Miguel de Cervantes en 1605."

# Hacer petición a la API
respuesta = requests.post(API_URL, headers=HEADERS, json={"inputs": texto})
resumen = respuesta.json()

# Mostrar resultado
print("Resumen generado por IA:", resumen)
