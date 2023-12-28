import re

email = input("What's your email? ").strip()

# if re.search(r"^..*@..*\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search(r"^\w+@\w+\.edu$", email):

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




[] set of characters allowed
[^] complementing the set (set of characters not allowed)


if re.search(r"^[^@]+@[^@]+\.edu$", email)

^: match from the start 
[^@]: "any char except @"
[^@]+: one or more "any char except @"

\.edu: followed by literally .edu

$: match at the end 

 



[a-zA-Z0-9_] 
replaced with \w



\w represents "word character"
which is commonly known as a alphanumeric symbol 



In Python's re module, which is used for working with regular expressions, 
\w is a special sequence that matches any alphanumeric character, 
including letters, numbers, and underscores. 

It's like a shortcut for matching common character types.

To break it down:

Alphanumeric characters: 
These are your basic letters and numbers. So, 
\w will match 
    'a', 'b', 'c', ..., 'z', 
    'A', 'B', 'C', ..., 'Z', 
    '0', '1', '2', ..., '9'.
    Underscores: It also matches the underscore character ('_').


    
"""