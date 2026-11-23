import numpy as np


data = np.array([
    [20, 30, 40],
    [50, 60, 70],
    [80, 90, 100],
    [10, 20, 30]
])

# Calculate the average of each row.
# Calculate the average of each column.
# Extract rows where the first column is greater than 30.
# Calculate the sum of all elements.
# Find the maximum value in each row.

avg_row = data.mean(axis=1)
print(avg_row)
avg_column = data.mean(axis=0)
print(avg_column)
f_great = data[0]
ff_great = f_great[f_great>30]
print(ff_great)
sum_all = data.sum()
print(sum_all)
max_zero = data.max(axis=1)
print(max_zero)
















