# Create a sample dictionary
student = {
    "name": "Harika",
    "age": 17,
    "course": "B.Tech CSE",
    "city": "Vijayawada"
}

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())

# Display all key-value pairs
print("Items:", student.items())

# Get a particular value
print("Name:", student.get("name"))

# Update dictionary
student.update({"age": 18, "city": "Guntur"})
print("After Update:", student)

# Remove an element using pop()
student.pop("city")
print("After Pop:", student)