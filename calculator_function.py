def add(a, b):
    print("Answer:", a + b)

def subtract(a, b):
    print("Answer:", a - b)

def multiply(a, b):
    print("Answer:", a * b)

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Answer:", a / b)


while True:
    print("\n===== Calculator =====")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation = input("Choose (+, -, *, /): ")

    if operation == "+":
        add(num1, num2)

    elif operation == "-":
        subtract(num1, num2)

    elif operation == "*":
        multiply(num1, num2)

    elif operation == "/":
        divide(num1, num2)

    else:
        print("Invalid operation")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again == "no":
        print("Goodbye!")
        break