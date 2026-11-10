# sales.csv uses -1 to mean "no sale" in the revenue column, and the string 
# "N/A" in the region column. Load it so both are treated as NaN. Then:
# Print how many rows have missing revenue
# Print the mean revenue excluding the -1 values
# # Compare that mean to what you'd get if you just did df.revenue.mean() 
# without specifying na_values

import pandas as pd
df = pd.read_csv("sales.csv",na_values={"revenue":[-1],"region":["N/A"]})
print(df["revenue"].isna().sum())
print(df["revenue"].mean())
df_raw = pd.read_csv("sales.csv")
print(df_raw["revenue"].mean())





