print("Welcome to the Calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition (+) \n2. Subtraction (-) \n3. Multiplication (*) \n4. Division (/)")

operator = input("Choose an operator: ")

if operator == '+' or operator.lower() == 'addition' or operator == '1' or operator.upper() == 'Addition':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-' or operator.lower() == 'subtraction' or operator == '2' or operator.upper() == 'Subtraction':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*' or operator.lower() == 'multiplication' or operator == '3' or operator.upper() == 'Multiplication':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == '/' or operator.lower() == 'division' or operator == '4' or operator.upper() == 'Division':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator. Please try again.")
