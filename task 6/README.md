
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

else:
    print("Reservation Confirmed!")
