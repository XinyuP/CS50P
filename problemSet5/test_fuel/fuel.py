def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    if percentage != None:
        print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        if int(y) == 0:
            raise ZeroDivisionError
        if int(x) > int(y): 
            raise ValueError
        return round((int(x) / int(y)) * 100)
            
    except ValueError:
        raise ValueError
    

def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{percentage}%"
        else:
            print("Percentage should be in the range 0-100")
            raise ValueError
    # if you compare a string with an integer using a relational operator like >, you'll encounter a TypeError
    except TypeError:
        raise TypeError
        
if __name__ == "__main__":
    main()

