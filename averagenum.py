# Read a CSV and compute the average of a numeric column.

with open("students.csv","r") as f:
    reader = f.readlines()[1:]
    average = [float(x.split(',')[2].strip()) for x in reader]

print(sum(average)/len(average))

