expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({
        "name": name,
        "amount": amount
    })

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    print("\n===== Expenses =====")

    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total}")


def remove_expense():
    if not expenses:
        print("No expenses found.")
        return

    name = input("Enter expense name to remove: ")

    for expense in expenses:
        if expense["name"].lower() == name.lower():
            expenses.remove(expense)
            print("Expense removed successfully.")
            return

    print("Expense not found.")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Remove Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            remove_expense()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()