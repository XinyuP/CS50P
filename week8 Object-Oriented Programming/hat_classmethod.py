import random

"""
singleton

We don't need to instantiate the sorting hat 
It already exists, we need just one


class variable
class method


instance variable
instance method


"""
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name): 
        print(f"{name} is in {random.choice(cls.houses)}")
    

# no need to instantiate a hat object

Hat.sort("Harry")









# def main():


# if __name__ == "__main__":
#     main()