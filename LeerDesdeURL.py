import pandas as pd 

dataURL = "http://winterolympicsmedals.com/medals.csv"

medalsData = pd.read_csv(dataURL)
print(medalsData.head)