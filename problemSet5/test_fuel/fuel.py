def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    if percentage != None:
        print(gauge(percentage))


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if int(x) > int(y): 
            raise ValueError
        return round((int(x) / int(y))*100)
            
    except ValueError:
        print("ValueError, x or y is not an integer")
        raise ValueError
    

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

