
# Progressive Electricity Billing System

months = int(input("Enter number of months: "))

bills = []

for i in range(months):
    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    # Calculate electricity charges using slabs
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        bill = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charge
    fixed_charge = 50

    # Surcharge
    surcharge = bill * 0.05

    # Rebate for low consumption
    rebate = 20 if units <= 100 else 0

    # Final bill
    total = bill + fixed_charge + surcharge - rebate

    bills.append({
        "month": month,
        "units": units,
        "amount": total
    })

    print("Energy Charge: Rs.", round(bill, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", rebate)
    print("Total Bill: Rs.", round(total, 2))

# Monthly bill comparison
print("\n===== MONTHLY BILL COMPARISON =====")

for i in range(len(bills)):
    print(bills[i]["month"], ":", round(bills[i]["amount"], 2))

# Identify unusual increases
print("\n===== UNUSUAL BILL INCREASES =====")

found = False

for i in range(1, len(bills)):
    previous = bills[i - 1]["amount"]
    current = bills[i]["amount"]

    increase = current - previous

    if increase > 0:
        percentage = (increase / previous) * 100

        if percentage > 50:
            print("Warning:", bills[i]["month"],
                  "bill increased by",
                  round(percentage, 2), "%")
            found = True

if not found:
    print("No unusual bill increases found.")
