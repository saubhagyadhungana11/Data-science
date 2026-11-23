import numpy as np

marks = np.array([45, 78, 90, 32, 67, 88, 54, 95, 73, 60])
# Calculate the average marks.
# Find the highest and lowest marks.
# Count students who scored above 75.
# Extract students who failed (marks below 40).
# Increase everyone's marks by 5.
# Calculate the percentage of students who passed (40 or above).

avg = marks.sum()/ len(marks)
print(avg)
highest = marks.max()
print(highest)
lowest = marks.min()
print(lowest)
above = marks[marks>75]
print(above)
fail = marks[marks<40]
print("Failed:",fail)
increase = marks+5  
print(increase)
passers = marks[marks>=40]
percent = passers.sum()/len(passers) * 100
print(percent)










