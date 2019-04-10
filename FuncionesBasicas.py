import pandas as pd
import numpy as np
import csv
import os

mainPath = "./DataSource"
fileName = "titanic3.csv"
fullName = os.path.join(mainPath, fileName)

#variable generica para los prints 
imprimirResultado = "Resultado {0}, {1}"
#print(imprimirResultado.format("prueba 01",25))

data = pd.read_csv(fullName, sep=",")
##Ver el encabezado
data.head

#Dimension del dataset (numero de filas y colmnas) el resultado viene en filas, columnas
data.shape

#Tail se usa para ver los ultimos registros
data.tail

#Columnas
data.columns
#Cabecera en un array de un df
data.columns.values

#Funciones estadisticas basicas de un DF para las variables numericas
basicas = data.describe()

#Ver los tipos de datos de un DF
data.dtypes

#comprobar si faltan valores en un DF
#arroja todos las filas
nulos = pd.isnull(data["body"])
noNulos = pd.notnull(data["body"])

nulos = nulos.values.ravel().sum()
noNulos = noNulos.values.ravel().sum()
# print("Valores faltantes %d y valores no faltantes %d" %(nulos, noNulos))

#Borrando los valores que faltan

data2 = data.dropna(axis=1) #Borra todas las columnas
data3 = data.dropna(axis=0) #Borra todas las filas que tienen NA
# print(data.shape)
# print(data2.shape)
# print(data3.shape)

data4 = data.dropna(axis=0, how="all") #Borra si cada una de las columnas son NA
# print(data4)

#Si al menos una de  las columnas tiene NA
data5 = data.dropna(axis=0, how="any")
# print(data5.shape) 

#En lugar de borrar los datos lo inferimos
#Imputacion o computo de los valores faltantes
# data6 = data.fillna(0) ##llena todos los na con un cero
#data6 = data.fillna("Desconocido")
# print(data6.head)

data6 = data
#Reemplazar dependiendo de la columna
data6["body"] = data6["body"].fillna(0)
data6["home.dest"] = data6["home.dest"].fillna("No Disponible")

##Llenar con el promedio la columna
#data6["age"] = data6["age"].fillna(data["age"].mean())

##Se puede reemplazar tambien por el valor siguiente
# data6["age"] = data6["age"].fillna(method="ffill")

##O por el anterior
data6["age"] = data6["age"].fillna(method="backfill")


print('data6["age"]: ', data6["age"])

