# transactions.csv has a date column in format DD/MM/YYYY. Pandas loads it as 
# object. Convert it to datetime, then add a month column and a weekday column
# . Print the count of transactions per weekday.

import pandas as pd

df = pd.read_csv("transaction.csv")
df["date"] = pd.to_datetime(df["date"],dayfirst=True)
df["month"] = df["date"].dt.month
df["weekday"] = df["date"].dt.weekday
print(df["weekday"].value_counts())
