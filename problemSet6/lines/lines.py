import sys
import os
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not os.path.splitext(sys.argv[1])[1] == ".py":
    # elif not sys.argv[1].endswith(".py"):
         sys.exit("Not a Python file")
    file_name  = sys.argv[1]
    print(get_count(file_name))


def get_count(file_name):
    try:
        count = 0
        with open(file_name) as file:
            for line in file:
                if not line.strip() or line.lstrip().startswith("#") or line.isspace():
                    continue
                count += 1
        return count
    
    except FileNotFoundError:
        sys.exit("File does not exist")
    

if __name__ == "__main__":
    main()





