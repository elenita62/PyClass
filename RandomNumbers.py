from Config import CargaArchivos as ca
import numpy as np
import random

datos = ca().data

#Generar un numero aleatorio entero entre 1 y 100
for x in range(10): #el range genera un array que inicia en 1 y en este caso termina en 10
    rd = np.random.randint(1, 100)
    # print('rd: ', rd);
    x -= 1

#La forma mas clasicas de generar un numero aletaroio es entre 0 y 1
for x in range(10):
    rdn = np.random.random()
    # print('rdn: ', rdn)
    x -= 1

#Funcion que genera una lista de n numeros aletarios enterios dentro del intervalo [a,b]
def randintList(n, a, b):
    x = []
    for i in range(n):
        x.append(np.random.randint(a, b))
    return x

# print(randintList(25, 1, 50))


def genera(cantElementos, desde, hasta):
    resultado = [] 
    for y in range(cantElementos):
        resultado.append(np.random.randint(desde, hasta))
    return resultado

#Usando la libreria Random
for x in range(10):
    aleatorio = random.randrange(0, 100, 5) #Multiplos de 5+0
    # print('aleatorio: ', aleatorio)
   
#Shuffling 
a = np.arange(100)
# print('a: ', a)
#cuando aplique el metodo shuffle, los datos se desordenan
np.random.shuffle(a)
# print('a: ', a)


#Choice para seleccionar un objeto de modo aleatorio
columnList = datos.columns.values.tolist()
# print('columnList: ', columnList)

#Elijo una columna al azar de una lista
for x in range(5):
    randomColumn = np.random.choice(columnList)
    print('randomColumn: ', randomColumn)