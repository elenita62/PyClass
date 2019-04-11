import pandas as pd
import os

mainPath = "./DataSource"
fileName = "Customer Churn Model.txt"
fullPath = os.path.join(mainPath, fileName)

data = pd.read_csv(fullPath, sep=",")

#Obtener las filas de la 1 a la 25
# print(data[0:25]) #Origen:Final
# print(data[:5]) #Es lo mismo que 0:5
# print(data[3320:]) #Es lo mismo que decir desde el 3320 hasta el final

##Filtrar por condicion
#Usuarios con Total Mins > 500
data2 = data[data["Day Mins"] >300]
# print('data: ', data2["Day Mins"])
# print(len(data2))
 
#Estados de NY
data3 = data[data["State"] == "NY"]
# print('data3: ', data3)

#Dos condiciones
#AND &
data4 = data[(data["Day Mins"]>300) & (data["State"]=="NY")]
# print('data4: ', data4)
# print(data4.shape)

#OR |
data5 = data[(data["Day Mins"]>300) | (data["State"] == "NY")]
# print(data5, len(data5))

#Comparando columnas
data6 = data[(data["Day Calls"] > data["Night Calls"])]
print('data6: ', data6[["Day Calls", "Night Calls"]])



