import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
         sys.exit("Not a CSV file")
    
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    convert(input_file_name, output_file_name)
    



def convert(input_file_name, output_file_name):
    try:
        with open(output_file_name, "w") as output_file:
            header = ["first", "last", "house"]
            output_writer = csv.DictWriter(output_file, fieldnames=header)
            output_writer.writeheader()
            try:
                with open(input_file_name) as input_file:
                    input_reader = csv.DictReader(input_file)
                    for student in input_reader: 
                        last, first = student["name"].split(", ")
                        house = student["house"]
                        output_writer.writerow({"first": first, "last": last, "house": house})
            except FileNotFoundError:
                sys.exit(f"Could not read {input_file}")


    except FileNotFoundError:
        sys.exit(f"Could not read {output_file}")

# def convert(input_file_name, output_file_name):
#     try:
#         with open(output_file_name, "w") as output_file:
#             header = ["first", "last", "house"]
#             output_writer = csv.DictWriter(output_file, fieldnames=header)
#             output_writer.writeheader()
#             try:
#                 with open(input_file_name) as input_file:
#                     input_reader = csv.reader(input_file)
#                     next(input_reader)
#                     for name, house in input_reader: 
#                         last, first = name.split(", ")
#                         output_writer.writerow({"first": first, "last": last, "house": house})
#             except FileNotFoundError:
#                 sys.exit(f"Could not read {input_file}")


#     except FileNotFoundError:
#         sys.exit(f"Could not read {output_file}")



if __name__ == "__main__":
    main()