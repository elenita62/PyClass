import pandas as pd
import numpy as np
import csv
import os

##Abriendo archivos con open
dataMainPath = "./datasource"

data3 = open(dataMainPath + "/Customer Churn Model.txt", 'r')
print(data3)
cols = data3.readline().strip().split(",")
n_cols = len(cols)
print(cols)
#print(n_cols)
counter = 0

mainDiccionario = {}
for col in cols:
    mainDiccionario[col] = []
    #sprint(col)

for line in data3:
    values = line.strip().split(",")
    for i in range(len(cols)):
        mainDiccionario[cols[i]].append(values[i])
    counter += 1

print("El dataset tiene %d filas y %d columnas"%(counter, n_cols))

##print(mainDiccionario)