import pandas as pd
import os
import matplotlib as mp
import matplotlib.pyplot as plt

mainPath = "./DataSource"
filePath = "Customer Churn Model.txt"
fullPath = os.path.join(mainPath, filePath)

data = pd.pandas.read_csv(fullPath)
# print('data: ', data.head(5))

#Scatterplot >> nube de dispersion o de puntos
# data.plot(kind="scatter", x="Day Mins", y="Day Charge")
#para mostrar el grafico
# plt.show(block=False)
# input("press <ENTER> to continue")

# data.plot(kind="scatter", x="Night Mins", y="Night Charge")
# plt.show(block=False)
# input("Press Enter")

#Para verlo en paneles
figure, axs = plt.subplots(2,2, sharex=True, sharey=True)
data.plot(kind="scatter", x="Day Mins", y="Day Charge", ax=axs[0][0])
data.plot(kind="scatter", x="Night Mins", y="Night Charge", ax=axs[0][1])
data.plot(kind="scatter", x="Day Calls", y="Day Charge", ax=axs[1][0])
data.plot(kind="scatter", x="Night Calls", y="Night Charge", ax=axs[1][1])
plt.show(block=False)
input("Press Enter")





