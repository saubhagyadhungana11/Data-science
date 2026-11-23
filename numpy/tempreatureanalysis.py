import numpy as np

temperature = np.array([25, 28, 30, 32, 29, 27, 35, 31])

# Average temperature.
# Days with temperatures above 30.
# Maximum temperature.
# Minimum temperature.
# How many days had temperatures between 25 and 30 (inclusive)

avg = temperature.mean()
print(avg)
above = temperature[temperature>30]
print(above)
max_temp = temperature.max()
print(max_temp)
min_temp = temperature.min()
print(min_temp)
between = temperature[(temperature>25) & (temperature<30)]
print(between)













