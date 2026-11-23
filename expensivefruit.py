# Task: Print the name of the most expensive fruit.

import csv

with open("fruits.csv", newline="") as f:
    rows = list(csv.DictReader(f))

if not rows:
    raise ValueError("No fruit data found.")

most_expensive = max(rows, key=lambda row: float(row["price"].strip()))
print(most_expensive["name"])
