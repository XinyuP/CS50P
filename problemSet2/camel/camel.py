# camel = input("camelCase: ")
# snake = ""
# i = 0
# for j in range(len(camel)):
#     if camel[j].isupper():
#         snake += camel[i:j].lower()
#         snake += "_"
#         i = j

# snake += camel[i:].lower()

# print(snake)



camel = input("camelCase: ")
snake = ""

for c in camel:
    if c.islower():
        snake += c
    else: 
        snake += "_" + c.lower()

print(snake)






























