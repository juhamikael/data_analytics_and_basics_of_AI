import pandas as pd


titanic_data = pd.read_csv("Titanic_data.csv")
titanic_names = pd.read_csv("Titanic_names.csv")

titanic_data.info()