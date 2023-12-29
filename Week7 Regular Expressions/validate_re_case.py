import re

email = input("What's your email? ").strip()


# if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE):
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



"""