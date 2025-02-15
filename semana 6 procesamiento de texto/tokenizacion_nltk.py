# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:37:14 2025

@author: jveraz
"""

####################################
# Tokenización y Análisis con NLTK #
####################################

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Descargar datos de NLTK
nltk.download("punkt")

# Texto de ejemplo: fragmento de un cuento
texto = "Había una vez un escritor llamado Borges. Sus cuentos eran laberintos de palabras."

# Tokenizar en oraciones
oraciones = sent_tokenize(texto)
print("Oraciones:", oraciones)

# Tokenizar en palabras
palabras = word_tokenize(texto)
print("Palabras:", palabras)
