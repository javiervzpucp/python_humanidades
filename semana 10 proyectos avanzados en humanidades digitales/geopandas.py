# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:55:19 2025

@author: jveraz
"""

############################################
# Proyecto: Mapas Históricos con Geopandas #
############################################

# REQUISITOS: Instalar geopandas antes de ejecutar
# pip install geopandas matplotlib

import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar un mapa de países del mundo
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Filtrar solo países de habla hispana
paises_hispanos = world[world["name"].isin(["Spain", "Mexico", "Argentina", "Peru", "Colombia"])]

# Graficar los países hispanohablantes
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color="lightgray")
paises_hispanos.plot(ax=ax, color="blue", edgecolor="black")

plt.title("Países de Habla Hispana en el Mundo")
plt.show()
