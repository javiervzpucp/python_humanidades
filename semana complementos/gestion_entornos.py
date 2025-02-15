# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:53:49 2025

@author: jveraz
"""

#############################################################
# Instalación de Librerías y Creación de Entornos Virtuales #
#############################################################

"""
Python permite instalar librerías adicionales para ampliar su funcionalidad.  
Muchas librerías usadas en Humanidades Digitales (geopandas, spacy, nltk, PIL, scikit-learn)  
requieren instalación previa.
"""

# **1. Instalación de Librerías**  
# Se instalan con pip desde la terminal o consola de comandos:
# pip install nombre_libreria
# Ejemplo:
# pip install geopandas spacy matplotlib scikit-learn requests

# **2. Creación de un Entorno Virtual (Recomendado)**
# Un entorno virtual permite instalar librerías sin afectar todo el sistema.
# Pasos:
# 1. Crear el entorno virtual:
#    Windows:  python -m venv mi_entorno
#    Mac/Linux:  python3 -m venv mi_entorno
#
# 2. Activar el entorno:
#    Windows:  mi_entorno\Scripts\activate
#    Mac/Linux:  source mi_entorno/bin/activate
#
# 3. Instalar librerías dentro del entorno:
#    pip install geopandas spacy nltk scikit-learn

# **3. Exportar e Importar Entornos**
# Para compartir el entorno con otros:
# pip freeze > requirements.txt  (Genera un archivo con todas las librerías)
#
# Para instalar todas las librerías en otro sistema:
# pip install -r requirements.txt

print("Consulta este script para instalar librerías y manejar entornos virtuales.")
