# Read a csv, group rows by a category column, and write a summary csv with 
# per category counts and averages of a numeric column.

import csv

group = {}

with open("categorize.csv", newline='') as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header
    for row in reader:
        category = row[0]
        value = float(row[1])
        group.setdefault(category, []).append(value)

with open("summary.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["category", "count", "average"])
    for cat, values in group.items():
        writer.writerow([cat, len(values), sum(values) / len(values)])   
        










