"""
template/mold

in order to store the attributes of the class,
we need to be able to store them in the current object that has just 
been instantiated 


self give you access to the current object that you just created 

"""
class Student: # invent a new data type called Student 
    def __init__(self, name, house, patronus): 
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            raise ValueError("Invalid house")        
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

    
def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

    # print(f'{student.name} from {student.house}')


# def get_student():  
#     student = Student() # creare an object of class, instantiating an object of Student class and assigning to a student variable
#     student.name = input("Name: ")
#     student.house = input("House: ") 

#     return student


# def get_student():  
#     name = input("Name: ")
#     house = input("House: ") 
#     return Student(name, house) # constructor call, instantiate a student object 
#     # call the Student() function, which is identical to the class name
#     # by defining a class, you get a function whose name is identical to the class name


def get_student():  
    name = input("Name: ")
    house = input("House: ") 
    patronus = input("Patronus: ")
    return Student(name, house, patronus)



if __name__ == "__main__":
    main()
    


"""
object is just an instance of class


__init__

  initialize the content of an object from a class

  initialize an otherwise empty object when you first create it

  initialization method.

  It initializes the value.


__new__
  a special method in python 
  handle the process of creating an empty object in memory for us 
  the programmer don't need to manipulate the __new__ function.
  It just works for you.

  

So there's technically a distinction between 

- constructing the object with __new__ and 
- initializing it with __init__

But in the world of Python, you only worry about the __init__ method

Python generally does the other part for you.





class - attributes

object - instance variables



- How are classes and objects represented in memory?

So the class is technically just code.
It is the code on the top of file that defines that blueprint, that template.

Objects are stored in the computer's memory by taking up some number of bytes.

You're probably familiar with bytes or kilobytes or megabytes.
There's some chunk of bytes, probably all in the same location in 
the computer's memory or RAM, where those objects are stored.
But that's what Python, the program, handles for you. Python the interpreter 
figures out where in the computer's memory to put it.

You and I, the programmers, get to think and solve problems at higher level.
Python, the interpreter, handles those lower level details for you.



"""