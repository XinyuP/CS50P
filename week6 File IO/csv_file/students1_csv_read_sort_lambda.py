"""
csv

split() returns a list of all the individual part to the left/right of the commas

rstrip() removes the end of each line in csv file 


"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")



######## sort list ########
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)



######## sort ########
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

# python allows you to pass functions as arguments into other functions 
# sorted() needs to know how to get the key of each student
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}") 
    # we need to use single quote



"""
when pass a function get_house/get_name to sorted() as the value of the key,
get_house/get_name is called automatically by sorted() on each of the object in the list
then it uses the return value of get_house/get_name to decide what strings to use to compare 
in order to decide which is alphabetically correct
    
sorted() use the value of key which is get_name, calling this function on every dictionary(object)
in the list that it is suppposed to sort, and the function get_name returns the string that sorted() 
will use to decided the order

sorted() decide the order based on the return value of get_name function

pass this function only by its name, do not pass with a () 
because we need the sorted() function to call this function for us, not us calling when passing into

"""
        
# #### sort lambda ####
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}") 
#     # we need to use single quote



######## sort lambda ########
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is in {student['house']}") 
    # we need to use single quote



        
"""
lambda function is anonymous function
a function that has no name


bc you don't need to give it a name if you're only gonna call it once in one place


lambda student: student["name"] 

is equivalent to

def get_name(student):
    return student["name"]

    

this function passed as a key is called on everyone of the students in the list

"""



# lambda student: student["name"] 

# # is equivalent to

# def get_name(student):
#     return student["name"]





"""
with open("students.csv") as file:
    for line in file:
        print(bytes(line, 'utf-8'))


b'Hermione,Gryffindor\n'
b'Harry,Gryffindor\n'
b'Ron,Gryffindor\n'
b'Draco,Slytherin'
        
"""