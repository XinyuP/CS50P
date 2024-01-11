import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file) # return a dictionary, one at a time
    print(type(reader)) # <class 'csv.DictReader'>
    for row in reader: # csv reader handles all the parsing of commas, new lines, and more 
        print(type(row)) # <class 'dict'>
        students.append({"name": row["name"], "home": row["home"]})
    
for student in sorted(students, key=lambda x: x["name"]):
    print(f"{student['name']} is from {student['home']}")
    

#################################################################
    
    
import csv

students = []

with open("students2.csv") as file:
    reader = csv.DictReader(file) # return a dictionary, one at a time
    for row in reader: # csv reader handles all the parsing of commas, new lines, and more 
        students.append(row)
    
for student in sorted(students, key=lambda x: x["name"]):
    print(f"{student['name']} is from {student['home']}")
    


