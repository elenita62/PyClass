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
# print('newSubSet: ', newSubSet.head(5))

#Otra forma excluyendo las no deseadas
#Obtenermos las columnas deseadas
desiredColumns = ["Account Length", "VMail Message", "Day Calls"]
allColumnsList = data.columns.values.tolist()
# print('allColumnsList: ', allColumnsList)

sublist = [x for x in allColumnsList if x in desiredColumns]
subSet2 = data[sublist]
# print('sublist: ', subSet2.head())


##Se puede hacer tambien restando
a = set(desiredColumns)
b = set(allColumnsList)
sublist2 = b - a 
sublist2 = list(sublist2)
print('sublist2: ', sublist2)