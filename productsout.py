# Write a script that outputs all products with stock == 0 to out_of_stock.csv
#  preserving the original header.

with open("products.csv",newline='') as f: 
    header = f.readline().strip()  # Read the header line
    with open("out_of_stock.csv", "w") as out_f:
        out_f.write(header + "\n")  # Write the header to the output file
        for line in f:
            fields = line.strip().split(",")
            stock = int(fields[2])  # Assuming stock is the third column (index 2)
            if stock == 0:
                out_f.write(line)  # Write the line to the output file if stock is 0
    











