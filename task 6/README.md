
# Railway Fare and Reservation Calculator

print("===== RAILWAY RESERVATION SYSTEM =====")

n = int(input("Enter number of passengers: "))

total_fare = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance (KM): "))

    print("\nTravel Classes")
    print("1. Sleeper - Rs. 2 per KM")
    print("2. AC 3 Tier - Rs. 4 per KM")
    print("3. AC 2 Tier - Rs. 6 per KM")

    choice = int(input("Select travel class (1-3): "))

    # Validate details
    if age <= 0 or distance <= 0 or choice not in [1, 2, 3]:
        print("Invalid passenger details!")
        continue

    # Select class fare
    if choice == 1:
        rate = 2
        class_name = "Sleeper"
    elif choice == 2:
        rate = 4
        class_name = "AC 3 Tier"
    else:
        rate = 6
        class_name = "AC 2 Tier"

    # Distance slab calculation
    if distance <= 100:
        base_fare = distance * rate
    elif distance <= 500:
        base_fare = 100 * rate + (distance - 100) * rate * 0.9
    else:
        base_fare = (100 * rate) + (400 * rate * 0.9) + (distance - 500) * rate * 0.8

    # Age-based concession
    if age < 12:
        concession = base_fare * 0.50
    elif age >= 60:
        concession = base_fare * 0.40
    else:
        concession = 0

    # Reservation fee
    reservation_fee = 50

    final_fare = base_fare - concession + reservation_fee

    print("\n----- PASSENGER FARE DETAILS -----")
    print("Name:", name)
    print("Age:", age)
    print("Class:", class_name)
    print("Distance:", distance, "KM")
    print("Base Fare: Rs.", round(base_fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Final Fare: Rs.", round(final_fare, 2))

    total_fare += final_fare

# Total reservation amount
print("\n===== TOTAL RESERVATION BILL =====")
print("Total Fare: Rs.", round(total_fare, 2))

# Cancellation calculation
cancel = input("\nDo you want to cancel the reservation? (yes/no): ")

if cancel.lower() == "yes":
    penalty = total_fare * 0.20
    refund = total_fare - penalty

    print("\n===== CANCELLATION DETAILS =====")
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund Amount: Rs.", round(refund, 2))
```mermaid
           
   flowchart TD
    A([Start]) --> B[/Enter Number of Passengers/]
    B --> C[/Enter Passenger Name, Age and Travel Distance/]
    C --> D[/Select Travel Class/]
    D --> E{Is Travel Class Valid?}
    E -- No --> F[Display Invalid Class]
    F --> D
    E -- Yes --> G{Is Distance Valid?}
    G -- No --> H[Display Invalid Distance]
    H --> C
    G -- Yes --> I[Calculate Base Fare According to Class]
    I --> J{Is Distance <= 100 KM?}
    J -- Yes --> K[Apply Full Rate]
    J -- No --> L{Is Distance <= 500 KM?}
    L -- Yes --> M[Apply 90 Percent Rate to Distance Above 100 KM]
    L -- No --> N[Apply 90 Percent Rate for 101-500 KM and 80 Percent Above 500 KM]
    K --> O[Calculate Fare]
    M --> O
    N --> O
    O --> P{Is Age Below 12?}
    P -- Yes --> Q[Apply 50 Percent Concession]
    P -- No --> R{Is Age 60 or Above?}
    R -- Yes --> S[Apply 40 Percent Concession]
    R -- No --> T[No Age Concession]
    Q --> U[Add Reservation Fee of Rs. 50]
    S --> U
    T --> U
    U --> V[Calculate Final Fare]
    V --> W{Is Reservation Cancelled?}
    W -- Yes --> X[Calculate 20 Percent Cancellation Penalty]
    W -- No --> Y[Confirm Reservation]
    X --> Z[Calculate Refund Amount]
    Y --> AA[/Display Passenger Fare and Reservation Details/]
    Z --> AA
    AA --> AB{Are More Passengers Available?}
    AB -- Yes --> C
    AB -- No --> AC([Stop])
```

else:
    print("Reservation Confirmed!")
