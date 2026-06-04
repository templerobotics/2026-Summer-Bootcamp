def conversion_main(input):
    selection = input(
        "Select the conversion type:\n1. Meters to Feet\n2. Inches to Centimeters\n3. Celsius to Fahrenheit\n"
    )
    value = input("Enter the value to convert: ")

    if selection == "1":
        return float(value) * 3.28084
    elif selection == "2":
        return float(value) * 2.54
    elif selection == "3":
        return float(value) * 1.8 + 32
    else:
        return "Invalid selection"


def main():
    result = str(round(conversion_main(input), 2))
    print("Converted value:", result)


main()
