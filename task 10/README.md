
# Campus Event Financial Planning System

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Get event details
event_name = input("Enter event name: ")

participants = int(input("Enter expected number of participants: "))

# Get event expenses
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

# Get financial support
sponsorship = float(input("Enter sponsorship amount: Rs. "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))

# Validate inputs
if (participants <= 0 or venue < 0 or equipment < 0 or
    catering < 0 or transport < 0 or certificate < 0 or
    sponsorship < 0 or registration_fee < 0):

    print("Invalid event details!")

else:
    # Calculate total expenses
    fixed_cost = venue + equipment + transport

    variable_cost = (catering + certificate) * participants

    total_cost = fixed_cost + variable_cost

    # Calculate participant contributions
    contribution = registration_fee * participants

    # Calculate sponsorship shortfall
    total_income = contribution + sponsorship

    shortfall = max(0, total_cost - total_income)

    # Calculate break-even registration count
    if registration_fee > (catering + certificate):
        required = (fixed_cost - sponsorship) / (
            registration_fee - catering - certificate
        )

        break_even = max(0, int(required) if required == int(required)
                         else int(required) + 1)

    else:
        break_even = None

    # Display financial report
    print("\n===== EVENT FINANCIAL REPORT =====")

    print("Event Name:", event_name)
    print("Expected Participants:", participants)

    print("\n----- EXPENSE DETAILS -----")
    print("Venue Cost: Rs.", venue)
    print("Equipment Cost: Rs.", equipment)
    print("Catering Cost: Rs.", catering * participants)
    print("Transport Cost: Rs.", transport)
    print("Certificate Cost: Rs.", certificate * participants)

    print("--------------------------------")
    print("Total Event Cost: Rs.", total_cost)

    print("\n----- INCOME DETAILS -----")
    print("Registration Contributions: Rs.", contribution)
    print("Sponsorship Amount: Rs.", sponsorship)
    print("Total Income: Rs.", total_income)

    print("Sponsorship/Financial Shortfall: Rs.", shortfall)

    print("\n----- BREAK-EVEN ANALYSIS -----")

    if break_even is not None:
        print("Minimum Registrations Required:", break_even)
    else:
        print("Break-even cannot be achieved with this fee.")

    if total_income >= total_cost:
        print("Event Financial Status: Budget Achieved")
    else:
        print("Event Financial Status: Budget Shortfall")
        Start the program.



Read the number of students.



Enter each student's name, roll number, aggregate marks, subject-wise marks, attendance, and family income.



Validate the entered details.



Check the eligibility conditions:
- Aggregate marks must be at least 75%.
- Subject-wise marks must be at least 60%.
- Attendance must be at least 75%.
- Family annual income must not exceed ₹2,00,000.



If all conditions are satisfied, add the student to the eligible list.



Otherwise, mark the student as not eligible.



Repeat the process for all students.



Sort eligible students by aggregate marks in descending order.



Resolve ties using:
- Higher subject-wise marks.
- Higher attendance.
- Lower family income.
- Lower roll number.



Assign ranks to eligible students.



Display eligible students and their rank
stop the progrem
Algorithm
1. Start the program.
2. Enter the number of participants.
3. Enter venue, equipment, and transport costs.
4. Enter catering and certificate costs per participant.
5. Enter the sponsorship amount.
6. Enter the registration fee per participant.
7. Calculate the total fixed cost.
8. Calculate the variable cost per participant.
9. Calculate the total event cost.
10. Calculate registration income and total income.
11. Compare total income with total event cost.
12. Determine whether there is a surplus or shortfall.
13. Calculate the minimum number of registrations required to break even.
14. Display the complete financial report.
15. Stop the program.
```mermaid
        
    flowchart TD
    A([Start]) --> B[/Enter Number of Participants/]
    B --> C[/Enter Venue Cost/]
    C --> D[/Enter Equipment Cost/]
    D --> E[/Enter Catering Cost per Person/]
    E --> F[/Enter Transport Cost/]
    F --> G[/Enter Certificate Cost per Person/]
    G --> H[/Enter Sponsorship Amount and Registration Fee per Person/]
    H --> I{Are All Inputs Valid?}
    I -- No --> J[Display Invalid Input]
    J --> B
    I -- Yes --> K[Calculate Total Fixed Cost]
    K --> L[Calculate Total Variable Cost]
    L --> M[Calculate Total Event Cost]
    M --> N[Calculate Registration Contributions]
    N --> O[Calculate Total Income Including Sponsorship]
    O --> P[Calculate Profit or Shortfall]
    P --> Q{Is Total Income >= Total Cost?}
    Q -- Yes --> R[Display Event Budget Surplus]
    Q -- No --> S[Calculate Sponsorship Shortfall]
    R --> T{Is Registration Fee Greater Than Variable Cost per Person?}
    S --> T
    T -- Yes --> U[Calculate Minimum Break-Even Participants]
    T -- No --> V[Display Break-Even Not Possible with Current Fee]
    U --> W[Generate Financial Report]
    V --> W
    W --> X[/Display Total Cost Income Shortfall and Break-Even Count/]
    X --> Y([Stop])
```
START

INPUT number of participants
INPUT venue cost
INPUT equipment cost
INPUT transport cost
INPUT catering cost per participant
INPUT certificate cost per participant
INPUT sponsorship amount
INPUT registration fee per participant

CALCULATE fixed cost
    fixed_cost = venue cost + equipment cost + transport cost

CALCULATE variable cost per participant
    variable_cost = catering cost + certificate cost

CALCULATE total variable cost
    total_variable_cost = variable_cost * number of participants

CALCULATE total event cost
    total_cost = fixed_cost + total_variable_cost

CALCULATE registration income
    registration_income = registration fee * number of participants

CALCULATE total income
    total_income = registration_income + sponsorship amount

CALCULATE financial result
    result = total_income - total_cost

IF result >= 0 THEN
    DISPLAY "Event has a surplus"
ELSE
    DISPLAY "Event has a shortfall"
END IF

CALCULATE break-even registration count

IF registration fee > variable cost THEN
    break_even = CEILING(
        (fixed_cost - sponsorship amount) /
        (registration fee - variable cost)
    )
    IF break_even < 0 THEN
        break_even = 0
    END IF
    DISPLAY break_even
ELSE
    DISPLAY "Break-even is not possible with this registration fee"
END IF

DISPLAY total cost
DISPLAY total income
DISPLAY result

STOP
======= CAMPUS EVENT FINANCIAL PLANNING =======

Enter number of participants: 100

Enter venue cost: 10000
Enter equipment cost: 5000
Enter transport cost: 3000

Enter catering cost per participant: 100
Enter certificate cost per participant: 20

Enter sponsorship amount: 8000
Enter registration fee per participant: 200

------------- FINANCIAL REPORT -------------

Fixed Cost: Rs. 18000
Variable Cost Per Participant: Rs. 120
Total Variable Cost: Rs. 12000

Total Event Cost: Rs. 30000

Registration Income: Rs. 20000
Sponsorship Amount: Rs. 8000

Total Income: Rs. 28000

Financial Result: Rs. 2000
Status: Shortfall

Minimum Registration Count for Break-Even: 82

--------------------------------------------
Thank you!
The Campus Event Financial Planning system calculates fixed and variable event costs, registration income, and sponsorship contributions. It identifies whether the event has a financial surplus or shortfall and determines the minimum number of registrations required to break even. This system helps colleges plan events, manage expenses, and make better financial decisions.
