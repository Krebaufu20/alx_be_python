num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}")
     case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
        result = num1 / num2
        print(f"The result is: {result}")
      case _:
        result = "Error: Invalid operation. please use +, -, *, or /."