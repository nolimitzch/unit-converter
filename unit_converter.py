# Convert kilometres to miles
def km_to_miles(km):
    return km * 0.621371

# Convert celsius to fahrenheight
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

# Convert kilograms to pounds
def kg_to_pounds(kg):
    return kg * 2.20462

#Convert miles to kilometres
def miles_to_kilometres (miles):
    return miles * 1.60934

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("That's not a number. Try again!")
# Text Menu
while True:
    print("\n--- Unit Converter ---")
    print("1. Kilometres to miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to pounds")
    print("4. Miles to kilometres")
    print("q. Quit")
    
    choice = input("Choose an option: ").strip().lower()
    
    if choice == "1":
        km = get_number("Enter kilometres: ")
        print(km, "km is", round(km_to_miles(km), 2), "miles")
    elif choice == "2":
        c = get_number("Enter degrees Celsius: ")
        print(c, "C is", round(celsius_to_fahrenheit(c), 1), "F")
    elif choice == "3":
        kg = get_number("Enter kilograms: ")
        print(kg, "kg is", round(kg_to_pounds(kg), 2), "pounds")
    elif choice == "4":
        miles = get_number("Enter miles: ")
        print(miles, "miles is", round(miles_to_kilometres(miles), 2), "km")
    elif choice == "q":
        print("Bye!")
        break
    else:
        print("Please choose 1, 2, 3 or q.")