# Create a nested dictionary
students = {
    1: {
        "name": "Harika",
        "marks": 90
    },
    2: {
        "name": "Priya",
        "marks": 85
    },
    3: {
        "name": "Sravani",
        "marks": 95
    }
}

# Print student names and marks
print("Student Details:")

for roll_no, details in students.items():
    print("Roll Number:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()