"""
lists are stored in the computer's memory, once your program exits, the content disappear


"""
names = []

for _ in range(3):
    names.append(input("What's your name? "))

    # name = input("What's your name? ")
    # names.append(name)

for name in sorted(names):
    print(f"hello, {name}")


"""
sorted(iterable)
return a new sorted list from the items in iterable














"""
























