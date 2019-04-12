import pandas as pd
import os

class CargaArchivos():
    fullPath = "./DataSource"
    filePath = "Customer Churn Model.txt"
    fileName = os.path.join(fullPath, filePath)
    data = pd.read_csv(fileName, sep=",")
    #Incluimos la columna de los minutos totales 
    data["Total Mins"] = data["Day Mins"] + data["Night Mins"] + data["Eve Mins"]
    #Incluimos columna con el total de las llamadas
    data["Total Calls"] = data["Day Calls"] + data["Night Calls"] + data["Eve Calls"]
