def get_user_input():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    return string1, string2


def concatenate_strings(string1, string2):
    return string1 + string2


def find_common_characters(string1, string2):
    return ''.join(char for char in string1 if char in string2)


def reverse_strings(string1, string2):
    return string1[::-1], string2[::-1]


menu_options = {
    1: "Concatenate Strings",
    2: "Find Common Characters",
    3: "Reverse Strings",
    4: "Exit"
}

while True:
    print("\nMenu:")
    for option, description in menu_options.items():
        print(f"{option}. {description}")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        string1, string2 = get_user_input()
        result = concatenate_strings(string1, string2)
        print(f"Concatenated String: {result}")

    elif choice == 2:
        string1, string2 = get_user_input()
        result = find_common_characters(string1, string2)
        print(f"Common Characters: {result}")

    elif choice == 3:
        string1, string2 = get_user_input()
        reversed_string1, reversed_string2 = reverse_strings(string1, string2)
        print(f"Reversed String 1: {reversed_string1}")
        print(f"Reversed String 2: {reversed_string2}")

    elif choice == 4:
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
