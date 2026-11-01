
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

Algorithm
1. Start the program.
2. Enter the number of students.
3. Enter student name and roll number.
4. Enter aggregate marks, subject-wise marks, attendance percentage, and family income.
5. Check whether the entered details are valid.
6. Check the eligibility criteria:
   - Aggregate marks must be 75% or above.
   - Subject-wise marks must be 60% or above.
   - Attendance must be 75% or above.
   - Family income must be ₹2,00,000 or below.
7. If all conditions are satisfied, add the student to the eligible list.
8. Otherwise, mark the student as not eligible.
9. Repeat the process for all students.
10. Sort eligible students according to aggregate marks in descending order.
11. Resolve ties using:
    - Higher subject-wise marks.
    - Higher attendance percentage.
    - Lower family income.
    - Lower roll number.
12. Assign ranks to eligible students.
13. Display eligible students and their rankings.
14. Stop the program

```mermaid
       
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
START

INPUT number_of_students

CREATE eligible_list

FOR each student from 1 to number_of_students

    INPUT name
    INPUT roll_number
    INPUT aggregate_marks
    INPUT subject_marks
    INPUT attendance
    INPUT family_income

    IF aggregate_marks >= 75 AND
       subject_marks >= 60 AND
       attendance >= 75 AND
       family_income <= 200000 THEN

          ADD student to eligible_list

    ELSE
          DISPLAY "Not Eligible"
    END IF

END FOR

SORT eligible_list BY
    aggregate_marks DESCENDING,
    subject_marks DESCENDING,
    attendance DESCENDING,
    family_income ASCENDING,
    roll_number ASCENDING

ASSIGN RANKS TO ELIGIBLE STUDENTS

DISPLAY eligible students and their ranks

STOP
Enter Number of Students: 3

Enter Student 1 Details:
Name: Harika
Roll Number: 101
Aggregate Marks: 85
Subject Marks: 80
Attendance: 90
Family Income: 150000

Enter Student 2 Details:
Name: Veda
Roll Number: 102
Aggregate Marks: 78
Subject Marks: 70
Attendance: 85
Family Income: 180000

Enter Student 3 Details:
Name: Nomitha
Roll Number: 103
Aggregate Marks: 65
Subject Marks: 55
Attendance: 80
Family Income: 100000

        UNIVERSITY SCHOLARSHIP RESULTS

------------------------------------------------
Name       Roll No    Aggregate    Status    Rank
------------------------------------------------
Harika       101        85%       Eligible    1
Veda         102        78%       Eligible    2
Nomitha      103        65%       Not Eligible  -
------------------------------------------------

Scholarship Eligibility Criteria:
Aggregate Marks >= 75%
Subject Marks >= 60%
Attendance >= 75%
Family Income <= Rs. 2,00,000

Total Students: 3
Eligible Students: 2
Not Eligible Students: 1

Highest Ranked Student: Harika
Scholarship Status: Eligible

             End of Program
             The University Scholarship Allocation system successfully identifies eligible students based on aggregate marks, subject-wise marks, attendance, and family income. It ranks eligible students using predefined rules and resolves ties fairly. This system makes the scholarship selection process simple, accurate, transparent, and efficient.







