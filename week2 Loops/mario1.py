# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()



def main():
    print_square(3)
    print_square2(4)
    print_square3(5)

def print_square(size):
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()

def print_square2(size):
    for _ in range(size):
        print("#" * size)


def print_square3(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()