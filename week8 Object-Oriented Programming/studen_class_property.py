
class Student:
    def __init__(self, name, house): 
        self.name = name
        self.house = house
    

    def __str__(self):
        return f"{self.name} from {self.house}"


    # Getter
    @property
    def name(self):
        return self._name
       
    @property
    def house(self):
        return self._house


    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]: 
            raise ValueError("Invalid house")        
        self._house = house

    

def main():
    student = get_student()
    # student._house = "tower"
    print(student)


def get_student():  
    name = input("Name: ")
    house = input("House: ") 
    return Student(name, house)


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