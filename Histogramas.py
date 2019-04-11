import pandas as pd
import os 
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mainPath = "./DataSource"
fileName = "Customer Churn Model.txt"
file = os.path.join(mainPath, fileName)

data = pd.read_csv(file)

plt.hist(data["Day Calls"], bins="sturges")

#sturges = 1 / Log2(muestra)
# si quisiera hacerlo manual
# sturges = 1+int(np.ceil(np.log2(3333)))
# plt.hist(data["Day Calls"], bins=sturges)
#sturges es una regla que nos indica la cantidad de clases que se deben
#considerar en un histograma

#Otra forma de pasar bins es con rangos fijos
# plt.hist(data["Day Calls"], bins=[0,30,60,90,120,150])
#Se puede poner un valor unico fijo tambien
# plt.hist(data["Day Calls"], bins=15)

plt.xlabel("Nro de llamadas al dia")
plt.ylabel("Frecuencia")
plt.title("Histograma de llamadas al dia")
plt.show(block=False)
input("Press Enter")


# print('data: ', data.head(5)) 
