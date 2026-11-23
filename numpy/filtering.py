import numpy as np




numbers = np.array([12, 45, 67, 23, 89, 34, 90, 56])


# All numbers greater than 50.
# All even numbers.
# Numbers between 30 and 80.
# Numbers less than 40 or greater than 80.

greater = numbers[numbers>50]
print(greater)
even = numbers[numbers%2==0]
print(even)
nums = numbers[(numbers>30) & (numbers<80)]
print(nums)
lesser = numbers[(numbers<40) | (numbers>80)]
print(lesser)









