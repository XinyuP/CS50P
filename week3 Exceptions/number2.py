"""
try:

except:

else:

"""


# try:
#     x = int(input("What's x? "))
# except ValueError: # if something goes wrong
#     print("x is not an integer")
# else: # if nothing goes wrong, do this
#     print(f"x is {x}")

# best
while True:
    try:
        x = int(input("What's x? "))
    except ValueError: # if something goes wrong
        print("x is not an integer")
    else: 
        break

print(f"x is {x}")



while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError: # if something goes wrong
        print("x is not an integer")

print(f"x is {x}")






"""


What's x? 12
x is 12
What's x? 23
x is 23
What's x? 43
x is 43
What's x? cat
x is not an integer
What's x? 12
x is 12
What's x? 
...


never end

"""
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError: # if something goes wrong
#         print("x is not an integer")
#     else:
#         print(f"x is {x}")





while True:
    try:
        x = int(input("What's x? "))
    except ValueError: # if something goes wrong
        print("x is not an integer")
    else:
        print(f"x is {x}")
        break


