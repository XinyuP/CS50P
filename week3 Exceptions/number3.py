def main():
    # x = get_int1()
    # print(f"x is {x}")


    # x = get_int2()
    # print(f"x is {x}")


    # x = get_int3()
    # print(f"x is {x}")
    

    x = get_int4("What's x? ")
    print(f"x is {x}")
    


def get_int1():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError: # if something goes wrong
            print("x is not an integer")
        else: 
            return x

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError: # if something goes wrong
#             print("x is not an integer")
#         else: 
#             break
#     return x
        

        
def get_int2():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError: # if something goes wrong
            print("x is not an integer")



##### pass #####
def get_int3():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError: # if something goes wrong
            pass


def get_int4(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError: # if something goes wrong
            pass


    # print(f"x is {x}")

main()