import pandas as pd
import os 
import matplotlib as mp
import matplotlib.pyplot as plt

mainPath = "./DataSource"
fileName = "Customer Churn Model.txt"
file = os.path.join(mainPath, fileName)

data = pd.read_csv(file)

plt.hist(data["Day Calls"], bins=8)
plt.show(block=False)
input("Press Enter")
# print('data: ', data.head(5))
