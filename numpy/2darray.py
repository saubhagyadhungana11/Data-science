# Create a 2D array:

import numpy as np 
 
arr = np.array([[11,21,43],[33,43,50]])
print(arr)


# Using the same array:
# - Extract the first row.
# - Extract the last column.
# - Extract the number 50.
# # - Extract the first two rows.

first = arr[0,:]
print(first)
last = arr[:,0]
print(last)
number = arr[1,2]
print(number)
frow = arr[:2]
print(frow)







