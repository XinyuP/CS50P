import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.match(r"(\d{1,2}):?(\d?\d?) (AM|PM) to (\d{1,2}):?(\d?\d?) (AM|PM)", s):
        # print(time.groups())
        first_hour = int(time.group(1))
        first_minute = 0 if not time.group(2) else int(time.group(2))
        first_meridiem = time.group(3)
        second_hour = int(time.group(4))
        second_minute = 0 if not time.group(5) else int(time.group(5))
        second_meridiem = time.group(6)            


            # first_hour = int(time.group(1))
            # first_minute = int(time.group(2))
            # first_meridiem = time.group(3)
            # second_hour = int(time.group(4))
            # second_minute = int(time.group(5))
            # second_meridiem = time.group(6)

        if first_hour <= 0 or first_hour > 12 or first_minute < 0 or first_minute >= 60 or second_hour <= 0 or second_hour > 12 or second_minute < 0 or second_minute >= 60:
            print("yes")
            raise ValueError
        
        if first_meridiem == "PM" and first_hour != 12:
            first_hour += 12
        elif first_meridiem == "AM" and first_hour == 12:
            first_hour = 0

        if second_meridiem == "PM" and second_hour != 12:
            second_hour += 12
        elif second_meridiem == "AM" and second_hour == 12:
            second_hour = 0



        return f"{str(first_hour).zfill(2)}:{str(first_minute).zfill(2)} to {str(second_hour).zfill(2)}:{str(second_minute).zfill(2)}"



    else:
        raise ValueError


if __name__ == "__main__":
    main()
