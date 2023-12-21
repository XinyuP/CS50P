expression = input("What is the arithmetic expression: ")

x, y, z = expression.split(" ")

match y:
    case "+":
        print(float(float(x) + float(z)))
    
    case "-":
        print(float(float(x) - float(z)))
    
    case "*":
        print(float(float(x) * float(z)))

    case "/":
        print(float(float(x) / float(z)))