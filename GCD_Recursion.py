# Define a recursive function
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Get input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call the function
result = gcd(num1, num2)

# Display the result
print("GCD of", num1, "and", num2, "is:", result)