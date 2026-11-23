# Create an array containing numbers from 1 to 24.

# Convert it into:
# - A 4 × 6 array.
# - A 6 × 4 array.
# - A 2 × 3 × 4 array.

import numpy as np 

numbers = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

fourbysix = numbers.reshape(4,6)
sixbyfour = numbers.reshape(6,4)
twobythreebyfour = numbers.reshape(2,3,4)

print(fourbysix)
print(sixbyfour)
print(twobythreebyfour)






