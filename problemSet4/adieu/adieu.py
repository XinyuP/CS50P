import inflect

def main():
    say_adieu()

def say_adieu():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break
    
    print("Adieu, adieu, to " + p.join(names))

if __name__ == "__main__":
    main()








# def main():
#     say_adieu()

# def say_adieu():
#     names = []
#     while True:
#         try:
#             name = input("Name: ")
#             names.append(name)
#         except EOFError:
#             break
    
#     if len(names) == 1:
#         print("Adieu, adieu, to " + names[0])
#     elif len(names) == 2:
#         print("Adieu, adieu, to " + names[0] + " and " + names[1])
#     else:
#         print("Adieu, adieu, to ", end="")
#         for name in names[:-1]:
#             print(name, end=", ")
#         print("and ", end="")
#         print(names[-1])

# if __name__ == "__main__":
#     main()