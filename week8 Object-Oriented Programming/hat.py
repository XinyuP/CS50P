import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    def sort(self, name):
        print(f"{name} is in {random.choice(self.houses)}")
    

hat1 = Hat() # instantiate a hat object
hat2 = Hat() # instantiate a hat object

hat1.sort("Harry")

