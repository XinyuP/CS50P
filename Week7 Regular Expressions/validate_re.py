import re

email = input("What's your email? ").strip()

# if re.search(".+@.+", email):
if re.search(r"..*@..*\.edu", email):
    print("Valid")
else:
    print("Invali d")


"""
. any charater except a newline
* 0 or more repetitions 
+ 1 or more repetitions 
? 0 or 1 repetition 
{m} m repetitions
{m,n} range m through n repetitions



raw strings are strings that don't format special characters
each character is taken at face-value`


.+ 
is equivalent to 
..*



"""