# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:24:32 2025

@author: jveraz
"""

############################################################
# Mini Proyecto 5: Proyecto Final en Humanidades Digitales #
############################################################

print("Escoge un proyecto final:")
print("1. Mapas históricos con Geopandas")
print("2. Análisis de texto con Spacy o NLTK")
print("3. Procesamiento de imágenes con Pillow")
print("4. Análisis de datos con Scikit-learn")
print("5. Uso de APIs de IA en Humanidades")

opcion = int(input("Elige una opción (1-5): "))

if opcion == 1:
    import geopandas as gpd
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    print("Proyecto de mapas históricos iniciado...")

elif opcion == 2:
    import spacy
    nlp = spacy.load("es_core_news_sm")
    texto = "Miguel de Cervantes escribió Don Quijote en 1605."
    doc = nlp(texto)
    print("Entidades encontradas:", [(ent.text, ent.label_) for ent in doc.ents])

elif opcion == 3:
    from PIL import Image, ImageEnhance
    imagen = Image.open("manuscrito.jpg")
    contraste = ImageEnhance.Contrast(imagen).enhance(2)
    imagen.show()
    print("Imagen procesada.")

elif opcion == 4:
    from sklearn.feature_extraction.text import CountVectorizer
    textos = ["Don Quijote es un libro clásico", "Cervantes escribió literatura universal"]
    vectorizador = CountVectorizer()
    matriz = vectorizador.fit_transform(textos)
    print("Frecuencia de palabras:", matriz.toarray())

elif opcion == 5:
    import requests
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    respuesta = requests.post(API_URL, headers={"Authorization": "Bearer TU_CLAVE"}, json={"inputs": "El Quijote es una obra literaria."})
    print("Resumen generado por IA:", respuesta.json())
else:
    print("Opción no válida. Intenta de nuevo.")
