import pandas as pd
import os


mainPath = "./DataSource"
fileName = "Customer Churn Model.txt"
fullPath = os.path.join(mainPath, fileName)

data = pd.read_csv(fullPath, sep=",")

#Crear un subconjunto de datos
#Extraer un subconjunto del conjunto original

#Determinar cuantas filas tiene una columna
account_length = data["Account Length"]

#Cuando extraemos una columna, python nos devuelve un objeto de tipo serie
# print(type(account_length))

# print('account_length: ', account_length.head(10))
subset = data[["Account Length", "Phone", "Eve Charge", "Day Calls"]]
#print('subset: ', subset.head(10))
# print(type(subset)) #Resulta como dataframe


#OTRA FORMA 
desiredColumns = ["Account Length", "Phone", "Eve Charge", "Day Calls"]
newSubSet = data[desiredColumns]
print('newSubSet: ', newSubSet.head(5))

