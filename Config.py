import pandas as pd
import os

class CargaArchivos():
    fullPath = "./DataSource"
    filePath = "Customer Churn Model.txt"
    fileName = os.path.join(fullPath, filePath)
    data = pd.read_csv(fileName, sep=",")