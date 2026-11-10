# You receive employees.csv. Write code that loads it and prints: shape, 
# dtypes, first 5 rows, and count of missing values per column.

import pandas as pd

df = pd.read_csv("employees.csv")
print("Shape:",df.shape)
print("Dtypes",df.dtypes)
print("first 5 rows:",df.head())
print("Missing values:",df.isnull().sum())

