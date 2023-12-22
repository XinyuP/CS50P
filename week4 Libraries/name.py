"""
Command-Line Arguments


take input/argument from the command line


sys


sys.argv
argument vector 

The list of command line arguments passed to a Python script

argv[0] is the script name


"""

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("please provide your name")



######################################

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])



######################################

import sys

if len(sys.argv) != 2:
    print("Please provide 1 argument")
else:
    print("hello, my name is", sys.argv[1])
    


"""
sys.exit


it is better to keep your error handling seperate from the code we care about
we don't want to hide the actual code we care about in the else statement 

"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Print name tags
print("hello, my name is", sys.argv[1])












































