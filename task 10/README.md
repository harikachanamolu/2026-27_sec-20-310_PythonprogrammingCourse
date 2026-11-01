
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
