import re

# name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")



# use () to capture the first name and last name
# anything surrounded by () will be returned to us 


name = input("What's your name? ").strip()

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    # last, first = matches.groups()
    # name = f"{first} {last}"

    # last = matches.group(1) # # The first parenthesized subgroup.
    # first = matches.group(2) # # The second parenthesized subgroup.
    # name = f"{first} {last}"

    # print(matches.group(0)) # The entire match
 
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")




"""

Cleaning Up User Input

capture 

(...)

when specify () in regex

everything in the () will be returned as a return value from re.search
It allows you to extract specific amounts of info from the user's input

We can reverse this process by using non-capturing version


non-capturing version
(?:...)




"""