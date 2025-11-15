import math

while True:
    # Safe input for first number
    try:
        a = float(input("Enter first number: "))
    except ValueError:
        print("Invalid number! Please enter digits only.")
        continue
    
    op = input("Enter operator (+, -, *, /, %, **, //, sqrt, sq, cube): ").strip()

    # Validate operator BEFORE asking for second number
    valid_ops = ["+", "-", "*", "/", "%", "**", "//", "sqrt", "sq", "cube"]
    if op not in valid_ops:
        print("Invalid operator!")
        continue
    
    # Only ask for second number if needed
    if op not in ["sqrt", "sq", "cube"]:
        try:
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter digits only.")
            continue

    # Operator logic
    try:
        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            print("Result:", a / b)
        elif op == "%":
            print("Result:", a % b)
        elif op == "**":
            print("Result:", a ** b)
        elif op == "//":
            print("Result:", a // b)
        elif op == "sqrt":
            print("Result:", math.sqrt(a))
        elif op == "sq":
            print("Result:", a * a)
        elif op == "cube":
            print("Result:", a * a * a)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    choice = input("Do you want to calculate again? (yes/no): ")
    if choice.lower() != "yes":
        break