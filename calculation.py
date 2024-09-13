print("1:sum 2:Sub 3:Mult 4:Div")
choice = input("Enter your choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print(f"sum = {num1 + num2}")
        elif choice == '2':
            print(f"Sub = {num1 - num2}")
        elif choice == '3':
            print(f"Mult = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"DIV = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
else:
        print("Invalid input, please select a valid operation (1/2/3/4).")
