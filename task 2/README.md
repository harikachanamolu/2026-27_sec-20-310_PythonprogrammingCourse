
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

```mermaid
       
flowchart TD
    A([Start]) --> B[/Enter Number of Months/]
    B --> C[/Enter Previous Month Units/]
    C --> D[/Enter Current Month Units/]
    D --> E{Are Units Valid?}
    E -- No --> F[Display Invalid Input]
    F --> D
    E -- Yes --> G{Units <= 100?}
    G -- Yes --> H[Calculate Bill at Rs. 2 per Unit]
    G -- No --> I{Units <= 200?}
    I -- Yes --> J[First 100 at Rs. 2 and Remaining at Rs. 3]
    I -- No --> K{Units <= 300?}
    K -- Yes --> L[First 100 at Rs. 2, Next 100 at Rs. 3, Remaining at Rs. 5]
    K -- No --> M[First 100 at Rs. 2, Next 100 at Rs. 3, Next 100 at Rs. 5, Remaining at Rs. 7]
    H --> N[Add Fixed Charge Rs. 50]
    J --> N
    L --> N
    M --> N
    N --> O[Calculate 5 Percent Surcharge]
    O --> P{Units <= 100?}
    P -- Yes --> Q[Apply Rs. 20 Rebate]
    P -- No --> R[No Rebate]
    Q --> S[Calculate Final Bill]
    R --> S
    S --> T[Store Monthly Bill]
    T --> U{More Months?}
    U -- Yes --> C
    U -- No --> V[Compare Monthly Bills]
    V --> W{Bill Increased More Than 50 Percent?}
    W -- Yes --> X[Display Unusual Increase Alert]
    W -- No --> Y[Display Normal Bill]
    X --> Z[Display Monthly Bills and Total]
    Y --> Z
    Z --> AA([Stop])
```
