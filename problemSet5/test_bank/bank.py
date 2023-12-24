def main():
    greeting = (input("Greeting: "))
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.strip().lower().startswith("h"):
        if greeting.strip().lower() == ("hello"):
            return 0
        else:
            return 20
    else:
        return 100
    
if __name__ == "main":
    main()