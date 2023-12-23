# import random

# def main():
#     guess_game()

# def guess_game():
#     while True: 
#         try:
#             level = int(input("Level: ").strip())
#             if level <= 0:
#                 continue
        
#         except (TypeError, ValueError):
#             pass
        
#         except (EOFError, KeyboardInterrupt):
#             break

#         else:
            
#             rd = random.randint(1, level)
#             while True:
#                 try:
#                     guess = int(input("Guess: ").strip())
#                     if guess <= 0:
#                         continue
                    
#                     if guess < rd:
#                         print("Too small!")
#                     elif guess > rd:
#                         print("Too large!")
#                     else:
#                         print("Just right!")
#                         break

#                 except (TypeError, ValueError):
#                     pass
                
#                 except (EOFError, KeyboardInterrupt):
#                     break
#             break



# if __name__ == "__main__":
#     main()




import random

def main():
    guess_game()

def guess_game():
    while True: 
        try:
            level = int(input("Level: ").strip())
            if level <= 0:
                continue

            rd = random.randint(1, level)
            while True:
                guess = int(input("Guess: ").strip())
                if guess <= 0:
                    continue
                
                if guess < rd:
                    print("Too small!")
                elif guess > rd:
                    print("Too large!")
                else:
                    print("Just right!")
                    return

        except (TypeError, ValueError):
            pass
        
        except (EOFError, KeyboardInterrupt):
            break
            



if __name__ == "__main__":
    main()





















