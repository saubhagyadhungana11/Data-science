# Load orders.csv, filter rows where amount > 100, and save the result to 
# large_orders.csv. Make sure the header row is written.

import pandas as pd

df = pd.read_csv("orders.csv")
items = df["amount"] > 100
df[items].to_csv("large_orders.csv",index=False)
    
    