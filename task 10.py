
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
