# months_dict = {
#     "January": 1,
#     "February": 2,
#     "March": 3,
#     "April": 4,
#     "May": 5,
#     "June": 6,
#     "July": 7,
#     "August": 8,
#     "September": 9,
#     "October": 10,
#     "November": 11,
#     "December": 12
# }

# def main():
#     get_date("Date: ")

# def get_date(prompt):
#     while True:
#         try:
#             date = input(prompt)
#             if date.find("/") != -1:
#                 month, day, year = map(int, date.strip().split("/"))
#                 if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0:
#                     print(f"{year:04d}-{month:02d}-{day:02d}")
#                     break
#             elif date.find(','):
#                 month, day, year = date.strip().split(" ")
#                 day = int(day[:-1])
#                 if 1 <= day <= 31 and int(year) >= 0:
#                     month = months_dict[month]
#                     print(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
#                     break
#         except KeyError:
#             print("Month does not exist")
#             break
#         except ValueError:
#             print("incorrect format")
#             pass
#         except (EOFError, KeyboardInterrupt):
#             print()
#             break

# main()






# months_list = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]


# def main():
#     get_date("Date: ")

# def get_date(prompt):
#     while True:
#         try:
#             date = input(prompt)
#             if date.find("/") != -1: # if "/" in date:
#                 month, day, year = list(map(int, date.split("/")))
#                 if 1 <= month <= 12 and 1 <= day <= 31 and year >= 0: 
#                     print(f"{year:04d}-{month:02d}-{day:02d}")
#                     break
#             elif date.find(',') != -1: # elif "," in date
#                 month, day, year = date.split(" ")
#                 day = int(day[:-1])
#                 if 1 <= day <= 31 and int(year) >= 0:
#                     month_num = months_list.index(month.title()) + 1
#                     print(f"{int(year):04d}-{month_num:02d}-{day:02d}")
#                     break
#         except ValueError:
#             print("incorrect format")
#         except (EOFError, KeyboardInterrupt):
#             print()
#             break

# main()






months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    get_date("Date: ")

def get_date(prompt):
    while True:
        try:
            date = input(prompt)
            if date.find("/") != -1: # if "/" in date:
                month, day, year = list(map(int, date.split("/")))
                
                if month < 0 or month > 12 or day < 0 or day > 31 or year < 0:
                    raise ValueError
                
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

            elif date.find(',') != -1: # elif "," in date
                month, day, year = date.strip().split(" ")
                day = int(day[:-1])

                if day < 0 or day > 31 or int(year) < 0:
                    raise ValueError
                
                month_num = months_list.index(month.title()) + 1
                print(f"{int(year):04}-{month_num:02}-{day:02}")
                break
            
        except ValueError as e:
            print("incorrect format", e)

        except (EOFError, KeyboardInterrupt):
            print()
            break

main()




"""

str.zfill(len)

add 0s at the beginning of the string, until it reaches the specified length

if the len is less than the length of the str, no filling is done


"""


# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]

# while True:
#     date = input("Date: ")
#     try:
#         if "/" in date:
#             mm, dd, yyyy = date.split("/")
#         elif "," in date:
#             mmdd, yyyy = date.split(", ")
#             mm, dd = mmdd.split(" ")
#             # No need to check if mm in months. KeyError is handled separately.
#             mm = (months.index(mm)) + 1
#         if int(mm) > 12 or int(dd) > 31:
#             raise ValueError
#     except (AttributeError, ValueError, NameError, KeyError):
#         pass
#     else:
#         print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
#         break