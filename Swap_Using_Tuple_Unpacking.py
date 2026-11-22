# Get two values from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display values before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using tuple unpacking
a, b = b, a

# Display values after swapping
print("After swapping:")
print("a =", a)
print("b =", b)