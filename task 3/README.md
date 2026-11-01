
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
        
