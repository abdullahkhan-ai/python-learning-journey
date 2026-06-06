import requests


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")

    if response.status_code == 200:
        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        print("\nQuote of the Day:")
        print(f'"{quote}"')
        print(f"- {author}")

    else:
        print("Failed to fetch quote.")


def main():
    while True:
        print("\n===== Quote Generator =====")
        print("1. Get Quote")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_quote()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
