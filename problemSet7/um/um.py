import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\b(um)\b", s, flags=re.IGNORECASE)
    return len(match)
    


if __name__ == "__main__":
    main()