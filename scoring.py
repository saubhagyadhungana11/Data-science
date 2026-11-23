# Task: Print how many students scored above 80.

import csv


with open("scores.csv",newline='') as f:
    score = sum(1 for line in csv.DictReader(f) if float(line["score"].strip()) > 80)
print(score)

