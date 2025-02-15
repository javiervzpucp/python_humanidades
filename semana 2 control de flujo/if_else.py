# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:15:33 2025

@author: jveraz
"""

############################################
# Condicionales en Python (if, else, elif) #
############################################

edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
elif edad == 18:
    print("Tienes exactamente 18 años.")
else:
    print("Eres mayor de edad.")
