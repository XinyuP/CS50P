import re
import sys


def main():
    print(convert(input("Hours: ")))


# def convert2(s):
#     if time := re.match(r"(\d{1,2}):?(\d?\d?) (AM|PM) to (\d{1,2}):?(\d?\d?) (AM|PM)$", s):
#         # print(time.groups())
#         first_hour = int(time.group(1))
#         first_minute = 0 if not time.group(2) else int(time.group(2))
#         first_meridiem = time.group(3)
#         second_hour = int(time.group(4))
#         second_minute = 0 if not time.group(5) else int(time.group(5))
#         second_meridiem = time.group(6)            

#         if first_hour <= 0 or first_hour > 12 or first_minute < 0 or first_minute >= 60 or second_hour <= 0 or second_hour > 12 or second_minute < 0 or second_minute >= 60:
#             print("yes")
#             raise ValueError
        
#         if first_meridiem == "PM" and first_hour != 12:
#             first_hour += 12
#         elif first_meridiem == "AM" and first_hour == 12:
#             first_hour = 0

#         if second_meridiem == "PM" and second_hour != 12:
#             second_hour += 12
#         elif second_meridiem == "AM" and second_hour == 12:
#             second_hour = 0

#         # return f"{str(first_hour).zfill(2)}:{str(first_minute).zfill(2)} to {str(second_hour).zfill(2)}:{str(second_minute).zfill(2)}"
#         return f"{first_hour:02}:{first_minute:02} to {second_hour:02}:{second_minute:02}"


#     else:
#         raise ValueError




def convert(s):
    if time := re.match(r"(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$", s):
        first_hour = int(time.group(1))
        first_minute = 0 if not time.group(2) else int(time.group(2))
        first_meridiem = time.group(3)
        second_hour = int(time.group(4))
        second_minute = 0 if not time.group(5) else int(time.group(5))
        second_meridiem = time.group(6)
        
        if first_meridiem == "PM" and first_hour != 12:
            first_hour += 12
        elif first_meridiem == "AM" and first_hour == 12:
            first_hour = 0

        if second_meridiem == "PM" and second_hour != 12:
            second_hour += 12
        elif second_meridiem == "AM" and second_hour == 12:
            second_hour = 0

        # return f"{str(first_hour).zfill(2)}:{str(first_minute).zfill(2)} to {str(second_hour).zfill(2)}:{str(second_minute).zfill(2)}"
        return f"{first_hour:02}:{first_minute:02} to {second_hour:02}:{second_minute:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()




# # others: 
    
# def convert(s):
#     regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
#     match = re.search(r"^" + regex + " to " + regex + "$", s)
#     if match:
#         from_time = standardize(match.group(1), match.group(2), match.group(3))
#         time = standardize(match.group(4), match.group(5), match.group(6))
#         return f"{from_time} to {time}"
#     else:
#         raise ValueError


# def standardize(hr, min, x):
#     if hr == "12":
#         if x == "AM":
#             hour = "00"
#         else:
#             hour = "12"
#     else:
#         if x == "AM":
#             hour = f"{int(hr):02}"
#         else:
#             hour = f"{int(hr)+12}"
#     if min == None:
#         minute = "00"
#     else:
#         minute = f"{int(min):02}"
#     return f"{hour}:{minute}"


# if __name__ == "__main__":
#     main()