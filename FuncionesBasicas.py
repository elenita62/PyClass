import pandas as pd
import numpy as np
import csv
import os

mainPath = "./DataSource"
fileName = "titanic3.csv"
fullName = os.path.join(mainPath, fileName)

data = pd.read_csv(fullName, sep=",")
##Ver el encabezado
#print(data.head)

#Dimension del dataset (numero de filas y colmnas) el resultado viene en filas, columnas
#print(data.shape)

#Tail se usa para ver los ultimos registros
#print(data.tail)

#Columnas
#print(data.columns)
#Cabecera en un array de un df
#print(data.columns.values)

#Funciones estadisticas basicas de un DF para las variables numericas
basicas = data.describe()
print(basicas)


