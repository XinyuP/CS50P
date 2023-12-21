"""
interpreter

side effect

bugs 

comments

pseudocode
    outline the program 
    nice way to structure the to do list 
"""


# print("What's your name?")
# input()

# Ask user for their name
name = input("What's your name? ") 
    # = assignment operator 
    # assign from right to left
    # = copy from the right to the left

# Say hellp to user
# string concatenation
print("hello," + name) # hello,Blaire
print("hello, " + name) # hello, Blaire
print("hello, " + name + name)# hello, BlaireBlaire

print("hello, ", name) # hello,  Blaire
print("hello,", name)  # hello, Blaire




#### str ####
print("hello, ")
print(name) 
# hello, 
# Blaire
# print function is automatically outputting a blank line 
# it moves the cursor automatically to the next line


"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

parameters to the function (what we can pass to a function)

when we use the function and pass in values inside of (), those input values are arguments

parameters: what the function can take 
arguments: what we are actually passing into the function

*objects: can take any number of objects   0,...inf

sep=' ': sep is short for seperator, default value for seperator is a single blank space


end='\n': default value for end is '\n', by default, this function is gonna end everyline with '\n'
'\n': backslash n, means newline, a way textually indicating when we want the computer 
    effectively to move the cursor to the next line, create a new line a text 


    
positional parameters: values we pass to print
named parameters: sep, end, etc. optional


"""

print("hello, ", end="")
print(name)
# hello, Blaire

print("hello, ", end="???")
print(name)
# hello, ???Blaire

print("hello,", name) # hello, Blaire
print("hello, ", name, sep = "") # hello, Blaire
print("hello,", name, sep = "???") # hello,???Blaire


print('hello, "friend"')   # hello, "friend"
print("hello, 'friend'")   # hello, 'friend'


#### escape character 
print("hello, \"friend\"") # hello, "friend" 
# literal quote




#### f string, format string
print("hello, {name}")  # hello, {name}
print(f"hello, {name}") # hello, Blaire



#### string methods
# What's your name?      blaire   
print(f"hello, {name}") 
# hello,      blaire


#### Remove whitespace from str
name = name.strip()
print(f"hello, {name}") 
# What's your name?       Blaire
# hello, Blaire

#### Capitalize user's name
name = name.capitalize()
print(f"hello, {name}") 
# What's your name?      blaire
# hello, Blaire

# What's your name?     blaire pang
# hello, Blaire pang

name2 = name.title()
print(f"hello, {name2}") 
# What's your name?     blaire pang
# hello, Blaire Pang



#### Remove whitespace from str and Capitalize user's name
name = name.strip().title()
print(f"hello, {name}") 
# What's your name?     blaire pang
# hello, Blaire Pang



# name4 = input("What's your name? ").strip().title()
# print(f"hello, {name4}") 
# # What's your name?     blaire Pang
# # hello, Blaire Pang


#### Split user's name into first name and last name
first, last = name.split(" ")
# What's your name? blaire pang
print(f"hello, {first}") # hello, Blaire
print(name.split(" ")) # ['Blaire', 'Pang']





#### int ####
"""

+
-
* 
/ 
% modulo operator -- remainder 


"""


#### interactive mode
