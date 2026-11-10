# customers.csv has a zip_code column with values like 07102, 04101. Load it 
# and print the unique zip codes. You'll see 7102, 4101 — the zeros are gone. 
# Fix the load so zips are preserved.

import pandas as pd 

df = pd.read_csv("customers.csv",dtype={"zipcode":str})
print(df["zipcode"].unique())






