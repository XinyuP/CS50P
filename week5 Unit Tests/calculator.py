def main():
    while True:
        try:
            x = int(input("What's x? "))
            print("x squared is", square(x))
        except ValueError:
            pass

def square(x):
    return x ** 2


if __name__ == "__main__":
    main()

# make sure when import square() in another file, treating it as a library
# make sure this main() is not automatically called itself in that file 
    




