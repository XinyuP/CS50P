"""
with 

in this context, I want you to open and automatically close the file



"""

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")


























# open the file in a way that allows me to change the content
# if file does not exist, create the file

# open returns a file handle, a special value that allows me to access that file subsequently
# file = open("names.txt", "w") # w rewrite the entire file
file = open("names.txt", "a") # a append to the end of the file

# write this person's name to this file
file.write(f"{name}\n")

# close , save the file 
file.close()



























