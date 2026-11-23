import numpy as np 

sales = np.array([1200, 1500, 900, 1800, 2000, 1700, 1100])

# Total weekly sales.
# Average daily sales.
# Highest sales day value.
# Lowest sales day value.
# Days when sales exceeded 1500.
# Increase all sales by 10%.

total_sales = sales.sum()
print(total_sales)
avg = sales.mean()
print(avg)
highest_sales = sales.max()
print(highest_sales)
lowest_sales = sales.min()
print(lowest_sales)
exceed = sales[sales>1500]
print(exceed)
increase = sales * 1.10 
add = sales + increase
print(add)








