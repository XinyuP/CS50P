"""
read from a file

readlines()
read all the lines from the file and return them as a list

"""


with open("names.txt", "r") as file:
    lines = file.readlines()
    # print(type(lines)) # <class 'list'>
for line in lines:
    print(f"hello, {line.rstrip()}")


# for line in lines:
#     line_byte = f"hello, {line}"
#     print(bytes(line_byte, 'utf-8'))

# b'hello, blaire\n'
# b'hello, hannah\n'
# b'hello, ted\n'
# b'hello, cindy\n'
# b'hello, Lucy'


######## combine them into one ########
# this is not able to sort the lines 
with open("names.txt", "r") as file:
    for line in file: # iterate every line in the file, one at a time 
        print(f"hello, {line.rstrip()}")



######## allow for the sorting ########
names = []

# if we just read, don't need to specify "r"
# "r" is default 
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")





######## sort on the file directly ########
with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")





######## reverse sorting ########
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"hello, {line.rstrip()}")












