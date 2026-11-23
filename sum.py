# Create a Python program that reads a file containing a list of numbers (one number per line)
# # and writes the sum of those numbers to another file called sum.txt.



with open("nums.txt","r") as f:
    reader = f.read()
    
total_sum = sum(int(num) for num in reader.split())
            
with open("sum.txt","w") as f:
    f.write(str(total_sum))

print("The total sum is:",total_sum)



