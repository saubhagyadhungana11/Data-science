# The Real Pipeline
# You have a folder raw/ containing jan.csv, feb.csv, mar.csv (same schema). 
# Each has:

# id (string, some have leading zeros)
# created_at (format MM/DD/YYYY HH:MM)
# status (uses "N/A" for missing)
# amount (some rows have "" instead of a number)
# Write a function load_all(raw_dir) that:

# Reads all three files with correct dtypes, date parsing, and na_values
# Concatenates them
# Adds a month column derived from created_at
# Drops rows where amount is missing
# Saves the result as combined.parquet
# Then write a second function load_clean() that just reads the Parquet file 
# and returns the DataFrame.
# Print: shape, dtypes, and amount.describe() for both the raw concat and the 
# Parquet reload. Confirm they're identical.
# Tests: glob/pathlib, all the read_csv params together, to_parquet/read_parquet, the "read once, reuse forever" habit

import pandas as pd

def load_all(raw_dir):
    files = ["jan.csv", "feb.csv", "mar.csv"]

    frames = []
    for f in files:
        df = pd.read_csv(
            f"{raw_dir}/{f}",
            dtype={"id": str},
            na_values={"status": ["N/A"], "amount": [""]},
            parse_dates=["created_at"],
            date_format={"created_at": "%m/%d/%Y %H:%M"},
        )
        frames.append(df)

    df = pd.concat(frames, ignore_index=True)
    df["month"] = df["created_at"].dt.month
    df = df.dropna(subset=["amount"])
    df.to_parquet("combined.parquet", index=False)
    return df


def load_clean():
    return pd.read_parquet("combined.parquet")   

