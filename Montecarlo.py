import numpy as np
import matplotlib.pyplot as plt
#Probabilidad de si elijo un punto cualquiera al azar dentro del cuadrado caiga dentro del circulo
#La simulacion de montecarlo 
#Primero generamos dos numeros aleatorios uniformes entre 0 y 1 (x e y)
#Luego calcularemos x * x + y * y (el área del círculo)
    #Si el valor es inferior a 1 estamos dentro del círculo
    #Si el valor es mayor que 1 estamos fuera del circulo
#Calculamos el nuero total de veces que estan dentro del circulo y lo dividimos entre el numero total de intentos para obtener una aproximacion
#de la probabilidad de caer dentro del circulo
#Usamos dicha probabilidad para aproximar el valor de pi 
#Repetimos el experimento un numero suficiente de veces (por ejemplo cien) para obtener (100) diferentes aproximaciones de pi
#Calculamos el promedio de los 1000 experimentos anteriores para dar un valor final

def piMontecarlo(n, nExp):
    piAVG = 0 
    n = 1000 #Numero de puntos
    piValueList = []
    for i in range(nExp):   #Numero de experimentos
        value = 0
        x = np.random.uniform(0, 1, n).tolist()
        y = np.random.uniform(0, 1, n).tolist()
        for j in range(n):
            z = np.sqrt(x[j] * x[j] + y[j] * y[j])
            if z<=1:
                value += 1
        float_value = float(value)
        piValue = float_value * 4 / n
        piValueList.append(piValue)
        piAVG += piValue
    pi = piAVG/nExp
    print('pi: ', pi)
    fig = plt.plot(piValueList)
    plt.show()
    return(pi, fig)

piMontecarlo(10000, 200)