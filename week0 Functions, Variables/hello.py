# def hello():
#     print("hello", end=", ")


# name = input("What's your name? ")

# hello()
# print(name)
# hello, blaire


def main():
    hello() # hello, world

    name = input("What's your name? ")
    hello(name) # pass name as argument
    # hello, Blaire


def hello(to="world"): # default value when programmer does not call hello with an argument 
    print("hello,", to)
    
main()
# hello, world
# What's your name? Blaire
# hello, Blaire



#### scope ####
# def main():
#     name = input("What's your name? ")
#     hello() # pass name as argument


# def hello(): # default value when programmer does not call hello with an argument 
#     print("hello,", name)
    
# main()