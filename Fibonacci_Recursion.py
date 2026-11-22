# Define a recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get input from the user
num = int(input("Enter the number of terms: "))

# Generate Fibonacci series
print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")