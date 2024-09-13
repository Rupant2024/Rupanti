print("1.celsius to fahrenheit")
print("2.fahrenheit to celsius")
Choice = input("choose conversion (1 or 2):")
if Choice == "1":
    celsius = float (input("Enter temperature in celsius:"))
    fahrenheit = (celsius * 9/5)+32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif Choice == "2":
    fahrenheit = float(input("Enter temperature in fahrenhite:"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("invalid choice, please 1 or 2.")
