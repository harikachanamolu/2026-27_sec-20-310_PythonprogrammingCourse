
# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN COST OPTIMIZATION =====")

# Get user requirements
usage = float(input("Enter monthly data usage (GB): "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

# Mobile plan details
plans = [
    {"name": "Basic Plan", "price": 199, "data": 2,
     "validity": 28, "extra": 20},

    {"name": "Standard Plan", "price": 299, "data": 10,
     "validity": 28, "extra": 15},

    {"name": "Premium Plan", "price": 499, "data": 20,
     "validity": 56, "extra": 10},

    {"name": "Unlimited Plan", "price": 699, "data": 50,
     "validity": 84, "extra": 5}
]

eligible = []

print("\n===== AVAILABLE PLAN DETAILS =====")

for plan in plans:

    # Calculate excess data charges
    excess = max(0, usage - plan["data"])
    extra_charge = excess * plan["extra"]

    total_cost = plan["price"] + extra_charge

    print("\nPlan:", plan["name"])
    print("Base Price: Rs.", plan["price"])
    print("Data Limit:", plan["data"], "GB")
    print("Validity:", plan["validity"], "days")
    print("Excess Charge: Rs.", extra_charge)
    print("Total Cost: Rs.", total_cost)

    # Check eligibility
    if (plan["validity"] >= validity and
        total_cost <= budget):

        eligible.append({
            "name": plan["name"],
            "cost": total_cost
        })

# Find economical plan
print("\n===== BEST MOBILE PLAN =====")

if len(eligible) == 0:
    print("No eligible mobile plan found.")

else:
    eligible.sort(key=lambda x: x["cost"])

    best = eligible[0]

    print("Most Economical Plan:", best["name"])
    print("Total Cost: Rs.", best["cost"])

    print("\nOther Eligible Plans:")
    for plan in eligible:
        print(plan["name"], "- Rs.", plan["cost"])
        ```mermaid
               Multi-Plan Telecommunications Cost Optimization: Evaluate several mobile plans against usage, validity, and budget constraints; calculate excess charges and identify the most economical eligible plan. 
               ```
