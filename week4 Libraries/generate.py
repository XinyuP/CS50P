"""
library
module


code written by you or others that you can use in your program


allow you to share functions or features with others as modules

a module in python is a library that has one or more functions or features built into it 

the purpose of a module or library is to encourage reusability of code 


"""


"""
random library

this module implements pseudo-random number generator for various distributions


random.choice(seq)

return a random element from the non-empty sequence seq
if seq is empty, raises IndexError

"""

# import everything in random module
import random

coin = random.choice(["heads", "tails"])

print(coin)
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))
print(random.choice(["heads", "tails"]))



# ############################################################

from random import choice

coin = choice(["heads", "tails"])



############################################################

"""
random.randint(a, b)

return a random number between a and b inclusive

return a random number a <= N <= b

same as randrange(a, b+1)

"""

import random
number = random.randint(1, 10) 

print(number)




############################################################

"""
random.shuffle(x)

shuffle the sequence x IN PLACE

shuffle an 

"""

import random


cards = ["jack", "queen", "king"]

random.shuffle(cards)

for c in cards:
    print(c )











