import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^..*@..*\.edu$", email):

    print(email, "Valid")
else:
    print(email, "Invalid")


"""
. any charater except a newline
* 0 or more repetitions 
+ 1 or more repetitions 
? 0 or 1 repetition 
{m} m repetitions
{m,n} range m through n repetitions



raw strings are strings that don't format special characters
each character is taken at face-value

-> Placing an r in front of the strings
tells the python interpreter to treat the string as a raw string,
similar to how placing an f in front of a string tells the python interpreter to
treat as a format string


eg.
\n in a reguar string becomes a special newline character
\n in a raw string is just a single "\" and a single "n"




.+ 
is equivalent to 
..*





^ matches the "start" of the string

$ matches the "end" of the string 
just befire the newline at the end of the string







re.search(r"^.+[@].+\.edu$", email)




[] set of characters
[^] complementing the set

if re.search(r"^[^@]+@[^@]+\.edu$", email)

^: match from the start 
[^@]: "any char except @"
[^@]+: one or more "any char except @"


\.edu: followed by literally .edu


$: match at the end 

 



"""