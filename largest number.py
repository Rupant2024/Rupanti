a = int(input("Enter a first number:"))
b = int(input("Enter a seceond number:"))
c = int(input("Enter a Third number:"))
if (a > b and a > c):
    print("{0} is Greater than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
    print("{0} is Greater than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
    print("{0} is Greater than both {1} and {2}". format(c, a, b))
else:
    print("Either any two values or All the three values are equal")
