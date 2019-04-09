# install anaconda-client
import pandas as pd
import csv
data = pd.read_csv(r"C:\Users\Elena López\Documents\GitHub\python-ml-course\datasets\titanic\titanic3.csv", sep=",")
#data.reader = csv.reader(data)
print(data.head)
    