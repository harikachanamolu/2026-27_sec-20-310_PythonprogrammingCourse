from functools import reduce

# Create a list
numbers = [1, 2, 3, 4, 5, 6]

# Using map() to find squares
squares = list(map(lambda x: x * x, numbers))

# Using filter() to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Using reduce() to find the sum
total = reduce(lambda x, y: x + y, numbers)

# Display the results
print("Original List:", numbers)
print("Squares using map():", squares)
print("Even Numbers using filter():", even_numbers)
print("Sum using reduce():", total)