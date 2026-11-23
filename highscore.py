# Read a CSV of students (name,age,score) and find the student with the 
# highest score.
import csv 

with open("students.csv","r") as f:
    reading = csv.DictReader(f)
    high_score = max(reading, key=lambda x: float(x["score"].strip()))


print(f"{high_score['name']} has the highest score of {high_score['score']}.")



