import numpy as np

marks = np.array([45, 67, 89, 76, 54])
# Total marks.
# Average marks.
# Highest marks.
# Lowest marks.
# Standard deviation.

total = marks.sum()
print(total)
avg = marks.sum()/ len(marks)
print(avg)
highest = marks.max()
print(highest)
lowest = marks.min()
print(lowest)
sd = marks.std()
print(sd)



