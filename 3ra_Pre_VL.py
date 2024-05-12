import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
#Vladimir Ariel Lizarro Velasquez
url='https://raw.githubusercontent.com/Uve-Lizarro/1er_Parcial_245_Vladimir_Lizarro/main/diabetes.csv'
datos=pd.read_csv(url)
def codifica_categoria():
    #La función codifica_categoria() utiliza la librería OneHotEncoder para codificar una categoría en binario.
    datos['categoria_edad']=pd.cut(datos['Age'], bins=3, labels=['Joven', 'Adulto', 'Adulto Mayor'])
    info=datos[['categoria_edad']]
    onehotencoder=OneHotEncoder()
    matriz=onehotencoder.fit_transform(info)
    print(matriz.toarray())
def normaliza_OneHotEncoder():
    #La función normaliza_OneHotEncoder() realiza lo mismo que la función normaliza() pero haciendo uso de la librería OneHotEncoder.
    carac_Num=datos.drop(columns=['Outcome'])
    scaler=StandardScaler()
    carac_Num_normalizadas=scaler.fit_transform(carac_Num)
    normalizado=pd.DataFrame(carac_Num_normalizadas, columns=carac_Num.columns)
    print(normalizado)
def normaliza():
    #La función normaliza() elimina los sesgos para mayor precisión en los datos, facilitando la comparación entre todas las características y así logrando una estabilidad numérica.
    dataset=datos[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']]
    escala=MinMaxScaler()
    normalizacion=escala.fit_transform(dataset)
    normalizado=pd.DataFrame(normalizacion, columns=dataset.columns)
    print(normalizado)
def discretizar():
    #La función discretizar() convierte las características numéricas en características discretas para reducir simplificar el modelo y reducir la complejidad computacional, además de permitir que el modelo sea más interpretable.
    valor_Discretizar='Age'
    datos['valor_Discretizar']=pd.cut(datos[valor_Discretizar], bins=5, labels=False)  
    print(datos[[valor_Discretizar, 'valor_Discretizar']])
def seleccion_Atributo():
    #La función seleccion_Atributo() selecciona los atributos más relevantes para poder realizar modelos predictivos.
    x=datos.drop('Outcome', axis=1)
    y=datos['Outcome']
    selector=SelectKBest(score_func=mutual_info_classif, k=2)
    aux=selector.fit_transform(x, y)
    indices=selector.get_support(indices=True)
    seleccionados=x.columns[indices]
    print("Atributos seleccionados:")
    for i in seleccionados:
        print(f"- {i}")
if __name__ == '__main__':
    seleccion_Atributo()
#