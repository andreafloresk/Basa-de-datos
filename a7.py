# -*- coding: utf-8 -*-
"""a7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UXjtmR7rI8npxG71eV_VGoG_qtPgjv7M

## **A7-visualización de datos multivariantes**
"""

import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import matplotlib.pyplot as plt

path = "/content/drive/My Drive/a4/antropometria-dataset-1-1.csv"

df=pd.read_csv(path)
df.head(5)

df.columns= list(map(str,df.columns))
df.columns

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['sistol'].dropna(), bins=15, color='blue', alpha=0.7)
plt.title('Histograma de la Presión Sistólica (sistol)')
plt.xlabel('Presión Sistólica')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.hist(df['diastol'].dropna(), bins=15, color='green', alpha=0.7)
plt.title('Histograma de la Presión Diastólica (diastol)')
plt.xlabel('Presión Diastólica')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['peso'].dropna(), bins=50, color='orange', alpha=0.7)
plt.title('Histograma de Peso')
plt.xlabel('Peso')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.hist(df['cintura'].dropna(), bins=50, color='red', alpha=0.7)
plt.title('Histograma de Cintura')
plt.xlabel('Cintura')

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['sistol'], df['peso'], alpha=0.5)
plt.title('Diagrama de Dispersión entre Peso y Cintura')
plt.xlabel('Peso')
plt.ylabel('Cintura')
plt.show()

hombres = df[df['sexo'] == 1]
plt.figure(figsize=(8, 6))
plt.scatter(hombres['peso'], hombres['cintura'], alpha=0.5)
plt.title('Diagrama de Dispersión para Hombres: Peso vs. Cintura')
plt.xlabel('Peso (hombre_peso)')
plt.ylabel('Cintura (hombre_cintura)')
plt.show()

plt.figure(figsize=(12, 6))
hombres = df[df['cintura'] == 1]
plt.subplot(1,2,2)
plt.hist(df['cintura'].dropna(), bins=50, color='red', alpha=0.7)
plt.title('Histograma de Cintura')
plt.xlabel('Cintura')