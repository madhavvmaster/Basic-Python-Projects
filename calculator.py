try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operation mode (+, -, *, /): ")

    match op:
        case "+":
            print(f"The addition of {num1} and {num2} is {num1 + num2}.")
        case "-":
            print(f"The subtraction of {num1} and {num2} is {num1 - num2}.")
        case "*":
            print(f"The multiplication of {num1} and {num2} is {num1 * num2}.")
        case "/":
            print(f"The division of {num1} and {num2} is {num1 / num2}.")

except (ValueError, TypeError, ZeroDivisionError) as e:
    print(f"Error: {e}")                