import csv

students = []

with open("students2.csv") as file:
    reader = csv.reader(file) # read a csv file for you, deal with conner cases for you 
    for name, home in reader: # csv reader handles all the parsing of commas, new lines, and more 
        students.append({"name": name, "home": home})
    
for student in sorted(students, key=lambda x: x["name"]):
    print(f"{student['name']} is from {student['home']}")







# each row is returned as a list of strings




# students = []

# with open("students2.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)
    
# for student in sorted(students, key=lambda x: x["name"]):
#     print(f"{student['name']} is from {student['home']}")




































