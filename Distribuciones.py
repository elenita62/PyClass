#Distribucion Uniforme
import numpy as np
import matplotlib.pyplot as plt

desde = 1
hasta = 1000000
muestra = 2000

# dist = np.random.uniform(desde, hasta, muestra)
# # print('dist: ', dist)

# plt.hist(dist)
# plt.show()
# input("Presione Enter para continuar...")


# #Distribucion Normal
# distN = np.random.randn(100)
# x = range(1, 101)
# plt.plot(x, sorted(distN))
# # plt.hist(distN)
# plt.title("Titulo")
# plt.show()
# input("Press Enter to Continue...")


mu = 5.5
sd = 2.5
distribucion = mu + sd * np.random.randn(1000)
# plt.hist(distribucion)
# plt.show()
# input("Press Enter to Continue...")

#A la funcion randn le podemos pasar como parametro un conjunto de numeros o colecciones
dataN = np.random.randn(2,4) #Dos colleciones de 4 elementos cada uno
plt.hist(dataN)
plt.show()
input("Press Enter to Continue...")