
# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

# Get production details
product = input("Enter product name: ")

quantity = int(input("Enter production quantity: "))

material = float(input("Enter material cost per unit: Rs. "))
labour = float(input("Enter labour cost per unit: Rs. "))
wastage = float(input("Enter wastage cost per unit: Rs. "))
machine = float(input("Enter machine cost per unit: Rs. "))

selling_price = float(input("Enter selling price per unit: Rs. "))

profit_target = float(input("Enter expected profit percentage: "))

# Validate inputs
if (quantity <= 0 or material < 0 or labour < 0 or
    wastage < 0 or machine < 0 or selling_price < 0 or
    profit_target < 0):

    print("Invalid input! Enter valid values.")

else:
    # Calculate production cost
    unit_cost = material + labour + wastage + machine

    total_cost = unit_cost * quantity

    # Calculate total revenue
    revenue = selling_price * quantity

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Display manufacturing report
    print("\n===== PRODUCTION COST REPORT =====")

    print("Product Name:", product)
    print("Production Quantity:", quantity)

    print("\nCost Details Per Unit")
    print("Material Cost: Rs.", material)
    print("Labour Cost: Rs.", labour)
    print("Wastage Cost: Rs.", wastage)
    print("Machine Cost: Rs.", machine)

    print("\nUnit Manufacturing Cost: Rs.", unit_cost)
    print("Total Manufacturing Cost: Rs.", total_cost)
    print("Total Selling Revenue: Rs.", revenue)

    print("\nTotal Profit/Loss: Rs.", profit)
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    # Check profit target
    print("\n===== PROFITABILITY RESULT =====")

    if profit_percentage >= profit_target:
        print("Production meets the profit target.")
    else:
        print("Production does not meet the profit target.")

    print("Expected Profit Target:", profit_target, "%")
