def main():
    time = input("Time: ")
    converted_time = convert(time)
    
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    if time.endswith("a.m."):
        time = time.rstrip("a.m.")
        # time = time.removesuffix("a.m.")
        hour, minute = time.split(":")

    elif time.endswith("p.m."):
        time = time.removesuffix("p.m.")
        hour, minute = time.split(":")
        if hour != "12":
            hour = float(hour) + 12
            
    else:
        hour, minute = time.split(":")
    
    return float(hour) + float(minute) / 60



if __name__ == "__main__":
    main()