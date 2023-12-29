import re

email = input("What's your email? ").strip()


# if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):

if re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):

    print("Valid")
else:
    print(email, "Invalid")


"""

Case Sensitivity


re.search(pattern, string, flags=0)

flags: 
re.IGNORECASE
re.MULTILINE
re.DOTALL



Scan through string looking for the first location where the regular expression
pattern produces a match, and return a corresponding Match. 

Return None if no position in the string matches the pattern; 

note that this is different from finding a zero-length match at some point in the string.




(\w+\.)? 0 or 1 subdomain
(\w+\.)* 0 or more subdomain



********
re.match(pattern, string, flags=0)

Don't need to specify the ^ symbol at the beginning
re.match automatically start matching from the beginning

re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match


********
re.fullmatch(pattern, string, flags=0)

Don't need to specify the ^ or & symbol
check both the match at the start and end of string

re.fullmatch("p.*n", "python") # Match
re.fullmatch("r.*n", "python") # No match





Document: 
re.match(pattern, string, flags=0)

If zero or more characters at the beginning of string match the regular expression pattern, 
return a corresponding Match.

Return None if the string does not match the pattern; 

note that this is different from a zero-length match.

Note that even in MULTILINE mode, re.match() will only match at the 
beginning of the string and not at the beginning of each line.

If you want to locate a match anywhere in string, use search() 
instead (see also search() vs. match()).




search() vs. match()
Python offers different primitive operations based on regular expressions:

re.search() checks for a match "anywhere" in the string (this is what Perl does by default)

re.match() checks for a match only at the "beginning" of the string

re.fullmatch() checks for "entire" string to be a match




Document: 

re.fullmatch(pattern, string, flags=0)
If the whole string matches the regular expression pattern, 
return a corresponding Match. 

Return None if the string does not match the pattern; 
note that this is different from a zero-length match.



"""