FILE_NAME = "students.txt"


def add_student():
    name = input("Enter student name: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "\n")

    print("Student added successfully.")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No students found.")
            return

        print("\n===== Students =====")

        for student in students:
            print(student.strip())

    except FileNotFoundError:
        print("No students found.")


def main():
    while True:
        print("\n===== File Student Management =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
