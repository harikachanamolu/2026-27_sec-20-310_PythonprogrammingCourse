# Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Create a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

# Display the results
print("Squares of numbers from 1 to 10:")
print(squares)

print("Even numbers from 1 to 10:")
print(even_numbers)