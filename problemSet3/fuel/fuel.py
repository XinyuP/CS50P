def main():
    x = get_int("Fraction: ")
    print(x)

def get_int(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            if int(x) > int(y): 
                print("x should be smaller than y")

            else:
                percent = round((int(x) / int(y))*100)
                if percent <= 1:
                    return "E"
                elif percent >= 99:
                    return "F"
                else:
                    return str(percent)+"%"
                
        except ValueError:
            print("x or y is not an integer")

        except ZeroDivisionError:
            print("y cannot be 0")
        # except (ValueError, ZeroDivisionError):
        #     pass



main()


