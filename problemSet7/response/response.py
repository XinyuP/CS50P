# from validator_collection import checkers
# def main():
#     print(validate_email(input("What's your email address? ")))


# def validate_email(email):
#     is_email_address = checkers.is_email(email)
#     if is_email_address:
#         return "Valid"
#     else:
#         return "Invalid"


# if __name__ == "__main__":
#     main()

import validators

def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(email):
    is_email_address = validators.email(email)
    if is_email_address:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()