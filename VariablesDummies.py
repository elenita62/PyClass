import pandas as pd
import numpy as np
import csv
import os

mainPath = "./DataSource"
fileName = "titanic3.csv"
fullPath = os.path.join(mainPath, fileName)

data = pd.read_csv(fullPath, sep=",")

dummySex = pd.get_dummies(data["sex"], prefix="sex")
# print('dummySex: ', dummySex.head)


#Agregamos las columnas creadas nuevas al dataset
column_name = data.columns.values.tolist()

#Combinamos el DS original con el data set dummy
data = pd.concat([data, dummySex], axis=1)
print('data: ', data)

#borramos la columna sex - tiene que ser un array

data.drop(["sex"], axis=1)

#Todo lo anteiror en una unica funcion
def generarVariableDummies (df, var_name):
    dummy = pd.get_dummies(df[var_name], prefix=var_name)
    df = df.drop([var_name], axis=1)
    df = pd.concat([df, dummy], axis=1)
    return df

newData = generarVariableDummies(data, "sex")