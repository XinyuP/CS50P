prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    get_cost("Item: ")



def get_cost(prompt):
    total_cost = 0
    while True:
        try:
            item = input(prompt).strip().title()
            total_cost += prices[item]
            print("Total: $", f"{total_cost:.2f}", sep="")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        except KeyError:
            print("Item does not exist")
        
    
main()


"""
The .2f format specifier indicates that you want to format the number 
as a float with two decimal places.
"""