"""

"""
def main():
    student = Student.get()
    print(student)


class Student:
    def __init__(self, name, house): 
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod # be able to call get() without having a student object in the universe already 
    def get(cls): # cls is a reference to the class itself 
        name = input("Name: ")
        house = input("House: ") 
        return cls(name, house) # cls automatically pass in reference to the class itself




if __name__ == "__main__":
    main()
    
