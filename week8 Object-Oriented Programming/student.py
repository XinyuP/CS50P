# def main():
#     # name, house = get_student()
#     # print(f"{name} from {house}")
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house # here means we are returning a tuple aka return (name, house)

# if __name__ == "__main__":
#     main()
    
##########################

# def main():
#     student = get_student()
#     print(f'{student["name"]} from {student["house"]}')


# def get_student():    
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] =input("House: ")
#     return student

# if __name__ == "__main__":
#     main()
    

##########################

# def main():
#     student = get_student()
#     print(f'{student["name"]} from {student["house"]}')


# def get_student():  
#     name = input("Name: ")
#     house = input("House: ")  
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()


##########################

def main():
    student = get_student()
    if student["name"] == "blaire":
        student["house"] = "Tower"
    print(f'{student["name"]} from {student["house"]}')


def get_student():  
    name = input("Name: ")
    house = input("House: ")  
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
    