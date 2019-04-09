# install anaconda-client
import pandas as pd
import numpy as np
import csv
import os

dataMainPath = "./datasource"
fileName = "titanic3.csv"
fullPath = dataMainPath + "/" + fileName
##Otra forma de hacer lo del path es con la siguiente funcion

fullPath2 = os.path.join(dataMainPath, fileName)

data = pd.read_csv(fullPath2, sep=",",dtype={"ingresos":np.float64, "edad":np.int32},
                   header=0, skip_blank_lines=True)
#data.reader = csv.reader(data)
#print(data)
    
 ##Cargando otro archivo, ahora tipo txt
fileNameTxt = "Customer Churn Model.txt"
fullPathTxt = os.path.join(dataMainPath, fileNameTxt)
data2 = pd.read_csv(fullPathTxt)
print(data2.head)

