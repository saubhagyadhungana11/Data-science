import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Perform:
# - Horizontal stacking.
# - Vertical stacking.
# - Concatenation.

horizontal = np.hstack((a,b))
print(horizontal)
vertical = np.vstack((a,b))
print(vertical)
concat = np.concatenate((a,b))
print(concat)











