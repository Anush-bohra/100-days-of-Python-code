# Day 10: Unit Converter

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462


while True:
    print("\n==== Unit Converter ====")
    print("1. Km → Miles")
    print("2. Miles → Km")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Kg → Lbs")
    print("6. Lbs → Kg")
    print("7. Exit")

    choice = input("Choose (1-7): ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")

    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")

    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print(f"{c} °C = {c_to_f(c):.2f} °F")

    elif choice == "4":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f} °F = {f_to_c(f):.2f} °C")

    elif choice == "5":
        kg = float(input("Enter Kg: "))
        print(f"{kg} kg = {kg_to_lbs(kg):.2f} lbs")

    elif choice == "6":
        lbs = float(input("Enter Lbs: "))
        print(f"{lbs} lbs = {lbs_to_kg(lbs):.2f} kg")

    elif choice == "7":
        print("👋 Exiting Converter...")
        break

    else:
        print("⚠ Invalid choice, try again.")
