from Config import CargaArchivos as ca

datos = ca().data
print(datos.head(4))

#Minutos de dia, de noche y longitud de la cuenta de los primeros 50 individuos
datos1 = datos[["Day Mins", "Night Mins", "Account Length"]][0:50] #El primer corchete es para condiciones de columnas, el segundo sobre las filas
# print('datos1: ', datos1)

#Otro modo usando la sintaxis usando ix, a traves de indices de filas o columnas
#Este metodo esta deprecado
# datos2 = datos.ix[1:10, 3:6] #Primero las filas que las columnas (al reves del ejemplo anterior) 
# print('datos2: ', datos2)

#ix se cambio por iloc
#Si vamos a acceder por indexado basado en posicion
# datos3 = datos.iloc[:,3:6] #Todas las filas y las columnas de la 3 a la 6
# datos3 = datos.iloc[1:10,:] #Las filas de la 1 a la 10 y todas las columnas
# datos3 = datos.iloc[1:10,[2,5,7]] #Primeras 10 filas y las columnas 2, 5, 7
# datos3 = datos.iloc[[1,5,8,36],[2,5,7]] #Filas 1, 5, 8 y 36 y las columnas 2, 5 y 7

#Si vamos a acceder por indexado basado en etiquetas o nombres de columnas
# datos3 = datos.loc[[1,5,8,36],["Area Code", "VMail Plan", "Day Mins"]]
# print('datos3: ', datos3)


print(datos[["Total Mins", "Day Mins", "Night Mins", "Eve Mins", "Total Calls", "Day Calls", "Night Calls", "Eve Calls"]][0:10])



