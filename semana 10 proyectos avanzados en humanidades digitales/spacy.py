# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:00 2025

@author: jveraz
"""

#########################################
# Proyecto: Análisis de Texto con Spacy #
#########################################

# REQUISITOS: Instalar spacy y el modelo en español antes de ejecutar
# pip install spacy
# python -m spacy download es_core_news_sm

import spacy

# Cargar modelo de español de Spacy
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
texto = "Miguel de Cervantes nació en Alcalá de Henares en 1547 y escribió Don Quijote."

# Procesar el texto con Spacy
doc = nlp(texto)

# Extraer entidades nombradas (lugares, fechas, nombres propios)
print("Entidades nombradas:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

# Extraer palabras clave (sustantivos y verbos)
print("\nPalabras clave:")
for token in doc:
    if token.pos_ in ["NOUN", "VERB"]:
        print(token.text, "-", token.pos_)
