text = (input("Input: ")).strip()
omit = ""
for c in text:
    if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
        omit += c
print(omit) 
