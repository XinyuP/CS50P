def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    omit = ""
    for c in word:
        if c.upper() not in {"A", "E", "I", "O", "U"}:
            omit += c
    return omit
    

if __name__ == "__main__":
    main()