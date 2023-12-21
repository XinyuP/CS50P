greet = (input("Greeting: ")).strip().lower()

if greet.startswith("h"):
    if greet.startswith("hello"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")