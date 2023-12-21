def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_length(s) and check_start_with(s) and check_number_middle(s) and check_periods_spaces_punctuation(s)
    
def check_start_with(s):
    return not s[0].isdigit() and not s[1].isdigit()

def check_length(s):
    return 2 <= len(s) <= 6

def check_number_middle(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            s = s[i:]
            return all([c.isdigit() for c in s])
    return all([not c.isdigit() for c in s])


def check_periods_spaces_punctuation(s):
    return all([c.isalnum() for c in s])


main()