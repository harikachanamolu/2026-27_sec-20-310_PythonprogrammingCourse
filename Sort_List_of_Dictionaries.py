# Create a list of student dictionaries
students = [
    {"name": "Harika", "marks": 90},
    {"name": "Priya", "marks": 85},
    {"name": "Sravani", "marks": 95},
    {"name": "Ravi", "marks": 75}
]

# Sort by marks in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

# Sort by marks in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

# Display ascending order
print("Students in Ascending Order:")
for student in ascending:
    print(student)

# Display descending order
print("\nStudents in Descending Order:")
for student in descending:
    print(student)