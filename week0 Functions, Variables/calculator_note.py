#### int ####

# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)
# # int() is also a function 
# print(z)

# # What's x? 1
# # What's y? 2
# # 3


# # What's x? -1
# # What's y? -4
# # -5


# x = int(input("What's x? "))
# y = int(input("What's y? "))
# print(x + y)

# # What's x? 1
# # What's y? 2
# # 3


# # What's x? -1
# # What's y? -4
# # -5





#### float ####
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)

# What's x? 1.2
# What's y? 2.3
# 3.5



"""
round(number[, ndigits])

takes just one number 
[ -> means optional


format long numbers
. for decimal 
, for seperartor

we want 1,000

"""

# What's x? 1.2
# What's y? 3.4
z = round(x + y)
print(z) # 5


# What's x? 999
# What's y? 1
# 1,000
print(f"{z:,}") # 1,000

# float cannot represent numbers infinitely precisely


z = x / y
print(z) # 0.6666666666666666

# int in python can be as big as we want them to be 
# there is no upper bound on how big an int can be in python 

# but there is a bound on just how precise a floating point value can be

z = round(x / y, 2)
print(z) # 0.67



z = x / y
print(f"{z:.2f}") # 0.67
print(f"{z:.4f}") # 0.6667


