# The Memory Problem
# logs.csv is 2 GB. You only need timestamp, user_id, and status_code. 
# Write code that:
# First loads 500 rows to inspect dtypes and missing values
# Then streams the full file in chunks of 100,000 rows, counting how many times 
# each status_code appears
# Print the final counts. Never load the full file into memory.
# Tests: usecols, nrows, chunksize

import pandas as pd
from collections import Counter

cols = ["timestamp","user_id","status_code"]

df = pd.read_csv("logs.csv",usecols=cols,nrows=500)

print(df.dtypes)
print(df.isna().sum())
counts = Counter()
for chunk in pd.read_csv("logs.csv", usecols=cols, chunksize=100_000):   
    counts.update(chunk["status_code"].value_counts().to_dict())
print(counts)















