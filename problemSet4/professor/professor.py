# import random

# def main():
#     level  = get_level()

#     score = 0
#     for _ in range(10):
#         x, y = generate_integer(level)
#         answer = input(f"{x} + {y} = ")
        
#         chance = 0
#         while (not answer.isdigit() or int(answer) != x + y) and chance < 2:
#             print("EEE")
#             answer = input(f"{x} + {y} = ")
#             chance += 1
        
#         if not answer.isdigit() or int(answer) != x + y:
#             print("EEE")
#             print(f"{x} + {y} = {x+y}")
#         else:
#             score += 1
    
#     print("Score:", score)


# def get_level():
#     while True:
#         try:
#             level = int(input("Level: "))
#             if level in (1, 2, 3):
#                 return level
#         except:
#             pass


# def generate_integer(level):
#     if level == 1:
#         x = random.randint(0, 9)
#         y = random.randint(0, 9)
#     else:
#         x = random.randint(10**(level-1), 10**level-1)
#         y = random.randint(10**(level-1), 10**level-1)
#     return x, y


# if __name__ == "__main__":
#     main()


import random

def main():
    level  = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        chance = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != x + y:
                    raise ValueError
                score += 1
                break

            except ValueError:
                print("EEE")
                chance += 1
                if chance > 2:
                    # print("EEE")
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    pass
                
            except (EOFError, KeyboardInterrupt):
                return
            
            

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    else:
        x = random.randint(10**(level-1), 10**level-1)
        y = random.randint(10**(level-1), 10**level-1)
    return x, y


if __name__ == "__main__":
    main()












