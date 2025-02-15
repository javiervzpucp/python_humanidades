# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:30:46 2025

@author: jveraz
"""

#################################################################
# Proyecto: Análisis de Datos Abiertos en Humanidades Digitales #
#################################################################
# En este proyecto, accederemos a datos abiertos de bibliotecas y archivos históricos.
# Usaremos la API de Wikidata para obtener información sobre autores y sus obras.
# Requisitos:
# Instalar requests si no está instalado:
#    pip install requests
# Ejecutar este script para obtener información en tiempo real.

import requests

# 🔹 Consulta SPARQL para obtener autores y sus obras desde Wikidata
consulta = """
SELECT ?autor ?titulo WHERE {
  ?libro wdt:P50 ?autor;
         wdt:P1476 ?titulo.
} LIMIT 5
"""

# 🔹 URL de la API de Wikidata
url = "https://query.wikidata.org/sparql"

# 🔹 Realizar la solicitud
respuesta = requests.get(url, params={"query": consulta, "format": "json"})

# 🔹 Extraer datos de la respuesta
datos = respuesta.json()
print("Autores y sus obras desde Wikidata:")
for item in datos["results"]["bindings"]:
    print(f"- {item['autor']['value']} → {item['titulo']['value']}")
