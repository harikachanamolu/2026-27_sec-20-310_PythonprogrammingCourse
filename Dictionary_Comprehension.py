# Create a dictionary using dictionary comprehension
squares = {x: x**2 for x in range(1, 11)}

# Display the dictionary
print("Dictionary of Numbers and Their Squares:")

for key, value in squares.items():
    print(key, ":", value)