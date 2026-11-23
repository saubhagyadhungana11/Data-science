# Read a CSV file and filter rows where a numeric column exceeds a threshold; 
# write those rows to a new CSV.

with open("students.csv","r") as f:
    reader = f.readlines()[1:]
    filtering = [x for x in reader if float(x.split(',')[2].strip()) > 45]

print(filtering)

with open("new_filtered.csv","a") as d:
    d.writelines(filtering)
    

