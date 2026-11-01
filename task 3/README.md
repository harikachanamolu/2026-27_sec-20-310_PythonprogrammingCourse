
# Hospital Billing and Patient Classification

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

# Get hospital charges
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate input
if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input! Please enter valid details.")

else:
    # Calculate total bill
    total = consultation + diagnostic + treatment

    # Apply concessions
    if age >= 60:
        discount = total * 0.20
    elif total >= 5000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("\n===== BILL DETAILS =====")
    print("Patient Name:", name)
    print("Total Charges: Rs.", total)
    print("Concession: Rs.", discount)
    print("Final Bill: Rs.", final_bill)

    # Payment details
    paid = float(input("Enter amount paid: "))

    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")

    else:
        balance = final_bill - paid

        # Patient classification
        print("\n===== PATIENT CLASSIFICATION =====")

        if balance == 0:
            print("Fully Paid Patient")
        elif paid > 0:
            print("Partially Paid Patient")
        else:
            print("Unpaid Patient")

        print("Amount Paid: Rs.", paid)
        print("Balance: Rs.", balance)
```mermaid
Algorithm
1. Start the program.
2. Enter the number of patients.
3. Enter patient name and age.
4. Enter consultation, diagnostic, and treatment charges.
5. Validate all charges. If invalid, ask the user to enter them again.
6. Calculate the total bill.
7. Check the concession rules:
   - If age is 60 or above, apply 20% concession.
   - Otherwise, if the total bill is ₹5,000 or above, apply 10% concession.
   - Otherwise, no concession is applied.
8. Calculate the final bill after concession.
9. Enter the amount paid by the patient.
10. Validate that payment is between zero and the final bill.
11. Classify the patient:
    - Fully Paid: Amount paid equals final bill.
    - Partially Paid: Amount paid is greater than zero but less than final bill.
    - Unpaid: Amount paid is zero.
12. Display the patient bill and payment classification.
13. Repeat for all patients.
14. Stop the program.
```mermaid        
    flowchart TD
    A([Start]) --> B[/Enter Number of Patients/]
    B --> C[/Enter Patient Name and Age/]
    C --> D[/Enter Consultation Charges/]
    D --> E[/Enter Diagnostic Charges/]
    E --> F[/Enter Treatment Charges/]
    F --> G{Are Charges Valid?}
    G -- No --> H[Display Invalid Charges]
    H --> D
    G -- Yes --> I[Calculate Total Bill]
    I --> J{Is Age 60 or Above?}
    J -- Yes --> K[Apply 20 Percent Concession]
    J -- No --> L{Is Total Bill 5000 or Above?}
    L -- Yes --> M[Apply 10 Percent Concession]
    L -- No --> N[No Concession]
    K --> O[Calculate Final Bill]
    M --> O
    N --> O
    O --> P[/Enter Amount Paid/]
    P --> Q{Is Payment Between Zero and Final Bill?}
    Q -- No --> R[Display Invalid Payment]
    R --> P
    Q -- Yes --> S{Is Payment Equal to Final Bill?}
    S -- Yes --> T[Classify as Fully Paid]
    S -- No --> U{Is Payment Greater Than Zero?}
    U -- Yes --> V[Classify as Partially Paid]
    U -- No --> W[Classify as Unpaid]
    T --> X[Display Patient Bill and Classification]
    V --> X
    W --> X
    X --> Y{Are More Patients Available?}
    Y -- Yes --> C
    Y -- No --> Z([Stop])
```   
     
START

INPUT number_of_patients

FOR each patient

    INPUT patient_name
    INPUT age

    INPUT consultation_charges
    INPUT diagnostic_charges
    INPUT treatment_charges

    IF any charge is negative THEN
        DISPLAY "Invalid Charges"
        INPUT charges again
    END IF

    total_bill = consultation_charges
                 + diagnostic_charges
                 + treatment_charges

    IF age >= 60 THEN
        concession = total_bill * 0.20
    ELSE IF total_bill >= 5000 THEN
        concession = total_bill * 0.10
    ELSE
        concession = 0
    END IF

    final_bill = total_bill - concession

    INPUT amount_paid

    WHILE amount_paid < 0 OR amount_paid > final_bill
        DISPLAY "Invalid Payment"
        INPUT amount_paid
    END WHILE

    IF amount_paid == final_bill THEN
        status = "Fully Paid"
    ELSE IF amount_paid > 0 THEN
        status = "Partially Paid"
    ELSE
        status = "Unpaid"
    END IF

    balance = final_bill - amount_paid

    DISPLAY patient_name
    DISPLAY total_bill
    DISPLAY concession
    DISPLAY final_bill
    DISPLAY amount_paid
    DISPLAY balance
    DISPLAY status

END FOR

STOP
Enter Patient Name: Harika
Enter Patient Age: 65
Enter Consultation Charges: 1000
Enter Diagnostic Charges: 2000
Enter Treatment Charges: 3000

Total Bill: Rs. 6000
Concession: 20%
Concession Amount: Rs. 1200
Final Bill: Rs. 4800

Enter Amount Paid: 3000

Remaining Balance: Rs. 1800
Patient Classification: Partially Paid

Hospital Bill Generated Successfully.
The Hospital Billing and Patient Classification system calculates patient bills by considering consultation, diagnostic, and treatment charges. It applies suitable concessions, validates payment details, and classifies patients as fully paid, partially paid, or unpaid. This system makes hospital billing accurate, simple, and efficient.
