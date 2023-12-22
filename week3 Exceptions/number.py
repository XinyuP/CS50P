"""

ValueError: invalid literal for int() with base 10: 'cat'
literal is just something we typed in 

* error handling *

try

except

"""


try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
    
print(f"x is {x}")

"""
NameError: name 'x' is not defined

"""
























