# Create a subject-marks dictionary
subjects = {
    "Python": 95,
    "Java": 90,
    "HTML": 85,
    "CSS": 88,
    "C++": 92
}

# Print dictionary keys
print("Subject Names:")
for key in subjects.keys():
    print(key)

# Print dictionary values
print("\nSubject Marks:")
for value in subjects.values():
    print(value)

# Print dictionary items
print("\nSubject and Marks:")
for key, value in subjects.items():
    print(key, ":", value)