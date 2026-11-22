# Define a function to calculate total and average
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Get marks from the user
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

# Call the function
total, average = calculate_marks(m1, m2, m3)

# Display the results
print("Total Marks:", total)
print("Average Marks:", average)