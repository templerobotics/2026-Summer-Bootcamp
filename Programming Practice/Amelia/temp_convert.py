def conversion_main():

    selection = input(
        "Select the conversion type:\n1. Meters to Feet\n2. Inches to Centimeters\n3. Celsius to Fahrenheit\n"
    )

    if selection not in ["1", "2", "3", "0"]:
        return "invalid selection"

    value = get_num_input("Enter the value to convert: ")

    if selection == "1":
        return float(value) * 3.28084
    elif selection == "2":
        return float(value) * 2.54
    elif selection == "3":
        return float(value) * 1.8 + 32
    elif selection == "0":
        return "Exiting the program."


def get_num_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    result = conversion_main()
    if isinstance(result, str):
        print(result)
    else:
        print("Converted value", round(result, 2))


if __name__ == "__main__":
    main()
