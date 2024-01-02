import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    # if re.search(r"^(?:(?:[1-9]?\d|1\d\d?|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d\d?|2[0-4]\d|25[0-5])$", ip):
    if re.search(r"^(?:(?:\d?|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$", ip):
        return True
    return False

if __name__ == "__main__":
    main() 