num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operation = input("Choose (+, -, *, /): ")

if operation == "+":
    print("Answer:", num1 + num2)

elif operation == "-":
    print("Answer:", num1 - num2)

elif operation == "*":
    print("Answer:", num1 * num2)

elif operation == "/":
    print("Answer:", num1 / num2)

else:
    print("Invalid operation")