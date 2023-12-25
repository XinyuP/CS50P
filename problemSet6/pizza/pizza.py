from tabulate import tabulate 
import csv
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
    file_name = sys.argv[1]
    table = get_table(file_name)
    print(table)



def get_table(file_name):
    try:
        with open(file_name) as file:
            reader = csv.reader(file) # <class '_csv.reader'>
            return tabulate(reader, headers="firstrow", tablefmt="grid")           
            
    except FileNotFoundError:
        sys.exit("File does not exist")




# def print_table(file_name):
#     try:
#         table = []
#         with open(file_name) as file:
#             reader = csv.reader(file) # <class '_csv.reader'>
#             for row in reader: # row is <class 'list'>
#                 table.append(row)
#     except FileNotFoundError:
#         sys.exit("File does not exist")

#     print(tabulate(table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()


















