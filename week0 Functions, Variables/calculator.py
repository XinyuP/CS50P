def main():

    x = int(input("What is x? "))
    print("x squared is", square(x))


def square(n):
    # return n * n
    # return n ** 2
    return pow(n, 2)
main()