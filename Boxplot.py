import pandas as pd
import os 
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

mainPath = "./DataSource"
fileName = "Customer Churn Model.txt"
file = os.path.join(mainPath, fileName)

data = pd.read_csv(file)


#El rango intercuantilico es la diferencia entre el cuartil 25 y el 75
#En el boxplot el bigote (lineas superiores e inferiores de la caja), se coloca a 1.5 el 
#rango intercuantilico como maximo

iqr = data["Day Calls"].quantile(0.75)-data["Day Calls"].quantile(0.25)
print('iqr: ', iqr)
#Esto es solo para entender el boxplot
#Por ejemplo, si queremos saber donde estara el bigote superior y el inferior de nuestro boxplot
bigoteSuperior = data["Day Calls"].quantile(0.75) + (iqr*1.5)
print('bigoteSuperior: ', bigoteSuperior)
bigoteInferior = data["Day Calls"].quantile(0.25) - (iqr*1.5)
print('bigoteInferior: ', bigoteInferior)


plt.boxplot(data["Day Calls"])
plt.ylabel("Nro. de llamadas diarias")
plt.title("Boxplot de las llamadas diarias")
plt.show(block=False)
input("Presiona enter para continuar")
