def conversion(input):
    selection = input(
        "Select conversion type:\n1. Meters to Feet\n2. Inches to Centimeters\n3.Celsius to Fahrenheit"
    )
    value = input("Enter value you want to convert")
    if selection == "1":
        return float(value) * 3.28
    elif selection == "2":
        return float(value) * 2.54
    elif selection == "3":
        return float(value) * 1.8 + 32
    else:
        return "Invalid selection"


def main():
    output = round(conversion(input), 2)
    print("Converted Value:", output)


main()
