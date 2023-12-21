### dict ####

# students = ["Hermoine", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# print(students["Hermoine"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])


"""
When we use a for loop in Python to iterate over a dict, by design, 
it iterate over all of the keys
"""
for student in students:
    print(student)


for student in students:
    print(student, students[student], sep=", ")




























