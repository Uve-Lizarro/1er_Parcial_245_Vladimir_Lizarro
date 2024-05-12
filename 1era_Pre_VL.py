import csv
import requests
from io import StringIO
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#Vladimir Ariel Lizarro Velasquez
url='https://raw.githubusercontent.com/Uve-Lizarro/1er_Parcial_245_Vladimir_Lizarro/main/diabetes.csv'
respuesta=requests.get(url)
dataset=StringIO(respuesta.text)
datos=[]
def primer_Inc():
    with dataset as file:
        lector=csv.reader(file)
        next(lector)
        for i in lector:
            datos.append(i)

    nroColumnas=len(datos[0])

    for i in range(nroColumnas):
        columna=[float(fila[i]) for fila in datos]
        columna.sort()
        for j, fila in enumerate(datos):
            fila[i]=columna[j]

    cuartil=[]
    percentil=[]

    for i in range(nroColumnas):
        columna=[float(row[i]) for row in datos]
        num_values=len(columna)

        q3_index=int(0.75*num_values)
        cuartil.append(columna[q3_index])

        p80_index=int(0.80*num_values)
        percentil.append(columna[p80_index])

    for i in range(nroColumnas):
        print(f"Columna {i+1}:")
        print(f"Último Cuartil: {cuartil[i]}")
        print(f"Percentil: {percentil[i]}")
        print("")
def segundo_Inc():
    datos=pd.read_csv(url)
    nroColumnas=len(datos.columns)
    
    cuartil=[]
    percentil=[]

    for i in range(nroColumnas):
        columna=datos.iloc[:, i].values
        q3_index=int(0.75*len(columna))
        cuartil.append(np.percentile(columna, 75))
        p80_index=int(0.80*len(columna))
        percentil.append(np.percentile(columna, 80))
    
    for i in range(nroColumnas):
        print(f"Columna {i+1}:")
        print(f"Último Cuartil: {cuartil[i]}")
        print(f"Percentil: {percentil[i]}")
        print("")
def tercer_Inc():
    with dataset as file:
        lector=csv.reader(file)
        next(lector)
        for fila in lector:
            datos.append(fila)
    matriz=pd.DataFrame(datos)
    matriz=matriz.iloc[:, :-1]
    matriz=matriz.apply(pd.to_numeric)
    media=np.mean(matriz)
    mediana=np.median(matriz)
    moda=stats.mode(matriz)[0][0]
    geometrica=stats.gmean(matriz)
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Geometrica: {geometrica}")
def cuarto_Inc():
    grafico=pd.read_csv(StringIO(respuesta.text))
    plt.figure(figsize=(10, 6))
    plt.scatter(grafico['Age'], grafico['DiabetesPedigreeFunction'], alpha=0.5)
    plt.title('Probabilidad de contraer Diabetes por Edades')
    plt.xlabel('EDAD')
    plt.ylabel('PROBABILIDAD')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    cuarto_Inc()