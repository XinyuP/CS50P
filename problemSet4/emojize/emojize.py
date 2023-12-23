import emoji


def main():
    get_emojize()

def get_emojize():
    emo = input("Input: ").strip()
    print(emoji.emojize("Output: " + emo, language='alias'))



if __name__ == "__main__":
    main()