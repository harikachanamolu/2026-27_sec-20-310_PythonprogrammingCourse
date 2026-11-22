# Define a function using *args
def calculate_sum(*args):
    total = 0
    for num in args:
        total = total + num
    return total

# Function calls
print("Sum of 2 numbers:", calculate_sum(10, 20))
print("Sum of 3 numbers:", calculate_sum(10, 20, 30))
print("Sum of 4 numbers:", calculate_sum(10, 20, 30, 40))
print("Sum of 5 numbers:", calculate_sum(10, 20, 30, 40, 50))