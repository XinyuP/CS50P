"""
walrus operator:
assigns a value from right to left and allows us to ask a boolean question at the same time. 

matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    ... 
    
is equivalent to 

if (matches := re.search(r"^(.+), *(.+)$", name)):
    ...

"""
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")


  
