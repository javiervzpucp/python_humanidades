# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:21:59 2025

@author: jveraz
"""

#############################################
# Mini Proyecto 1: Edad y Chatbot Literario #
#############################################

# 1. Preguntar el año de nacimiento del usuario y calcular su edad.
anio_nacimiento = int(input("¿En qué año naciste? "))
edad = 2025 - anio_nacimiento
print(f"Tienes aproximadamente {edad} años.")

# 2. Simular un chatbot que interactúe con el usuario usando condicionales.
print("\nChatbot Literario: Pregunta algo sobre literatura:")
pregunta = input("Tú: ")

if "autor" in pregunta.lower():
    print("Chatbot: Miguel de Cervantes escribió 'Don Quijote de la Mancha'.")
elif "libro" in pregunta.lower():
    print("Chatbot: 'Cien años de soledad' es una obra maestra de Gabriel García Márquez.")
else:
    print("Chatbot: No tengo información sobre eso, intenta otra pregunta.")
