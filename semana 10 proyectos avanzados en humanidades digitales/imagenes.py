# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:20 2025

@author: jveraz
"""

###########################################################
# Proyecto: Análisis de Imágenes en Humanidades Digitales #
###########################################################

# REQUISITOS: Instalar Pillow antes de ejecutar
# pip install pillow matplotlib

from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Cargar imagen de un manuscrito antiguo
imagen = Image.open("manuscrito.jpg")

# Aplicar mejora de contraste
contraste = ImageEnhance.Contrast(imagen)
imagen_mejorada = contraste.enhance(2)

# Mostrar imágenes original y mejorada
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(imagen)
axs[0].set_title("Imagen Original")
axs[0].axis("off")

axs[1].imshow(imagen_mejorada)
axs[1].set_title("Imagen Mejorada")
axs[1].axis("off")

plt.show()
