
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
```memaid
       
  flowchart TD
    A([Start]) --> B[/Enter Number of Students/]
    B --> C[/Enter Student Name, Roll Number/]
    C --> D[/Enter Aggregate Marks, Subject Marks, Attendance and Family Income/]
    D --> E{Are Input Values Valid?}

    E -- No --> F[Display Invalid Details]
    F --> C

    E -- Yes --> G{Aggregate Marks >= 75%?}

    G -- No --> H[Student Not Eligible]
    G -- Yes --> I{Subject Marks >= 60%?}

    I -- No --> H
    I -- Yes --> J{Attendance >= 75%?}

    J -- No --> H
    J -- Yes --> K{Family Income <= 200000?}

    K -- No --> H
    K -- Yes --> L[Add Student to Eligible List]

    H --> M{More Students?}
    L --> M

    M -- Yes --> C
    M -- No --> N[Sort Eligible Students by Aggregate Marks]

    N --> O{Aggregate Marks Equal?}
    O -- Yes --> P[Compare Subject Marks]
    P --> Q{Subject Marks Equal?}

    Q -- Yes --> R[Compare Attendance]
    R --> S{Attendance Equal?}

    S -- Yes --> T[Compare Family Income]
    T --> U{Income Equal?}

    U -- Yes --> V[Sort by Roll Number]
    U -- No --> W[Assign Rank]
    S -- No --> W
    Q -- No --> W
    O -- No --> W

    V --> W
    W --> X[/Display Eligible Students and Rankings/]
    X --> Y([End])
```







