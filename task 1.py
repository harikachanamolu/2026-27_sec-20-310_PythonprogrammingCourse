
# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter aggregate marks: "))
    subject = float(input("Enter minimum subject marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Eligibility checking
    if (marks >= 75 and subject >= 60 and
        attendance >= 75 and income <= 200000):

        students.append({
            "name": name,
            "roll": roll,
            "marks": marks,
            "subject": subject,
            "attendance": attendance,
            "income": income
        })

# Ranking eligible students
students.sort(
    key=lambda x: (
        -x["marks"],
        -x["subject"],
        -x["attendance"],
        x["income"],
        x["roll"]
    )
)

print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if len(students) == 0:
    print("No eligible students found.")

else:
    for rank, student in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Roll Number:", student["roll"])
        print("Aggregate Marks:", student["marks"])
        print("Subject Marks:", student["subject"])
        print("Attendance:", student["attendance"])
        print("Family Income:", student["income"])

print("\nTotal Eligible Students:", len(students))







