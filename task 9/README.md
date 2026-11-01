
# Multi-Currency Travel Budget Analysis

print("===== TRAVEL BUDGET ANALYSIS =====")

budget = float(input("Enter your total travel budget (INR): "))
n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0

for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (USD/EUR/GBP): ").upper()

    # Supplied exchange rates in INR
    rates = {
        "USD": 84,
        "EUR": 92,
        "GBP": 108
    }

    # Validate expense
    if amount < 0 or currency not in rates:
        print("Invalid amount or currency!")
        continue

    # Currency conversion
    converted = amount * rates[currency]

    # Conversion fee (2%)
    fee = converted * 0.02

    # Final expense in INR
    total = converted + fee

    total_spending += total

    expenses.append({
        "category": category,
        "amount": total
    })

    print("Converted Amount: Rs.", round(converted, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(total, 2))

# Find largest expense category
print("\n===== TRAVEL EXPENSE REPORT =====")

for item in expenses:
    print(item["category"], ": Rs.", round(item["amount"], 2))

print("\nTotal Spending: Rs.", round(total_spending, 2))
print("Travel Budget: Rs.", budget)

# Budget comparison
if total_spending > budget:
    print("Status: Budget Exceeded!")
    print("Extra Amount: Rs.", round(total_spending - budget, 2))
else:
    print("Status: Within Budget!")
    print("Remaining Budget: Rs.", round(budget - total_spending, 2))

# Largest expense
if len(expenses) > 0:
    largest = max(expenses, key=lambda x: x["amount"])

    print("\nLargest Expense Category:", largest["category"])
    print("Amount: Rs.", round(largest["amount"], 2))
else:
    print("No valid expenses entered.")
```mermaid
     
    flowchart TD
    A([Start]) --> B[/Enter Travel Budget in Base Currency/]
    B --> C[/Enter Number of Expense Categories/]
    C --> D[/Enter Category Name and Expense Amount/]
    D --> E[/Enter Foreign Currency and Exchange Rate/]
    E --> F{Is Input Data Valid?}
    F -- No --> G[Display Invalid Input]
    G --> D
    F -- Yes --> H[Convert Expense into Base Currency]
    H --> I[Calculate Conversion Fee]
    I --> J[Add Conversion Fee to Converted Amount]
    J --> K[Store Category Expense]
    K --> L{Are More Categories Available?}
    L -- Yes --> D
    L -- No --> M[Calculate Total Travel Expenses]
    M --> N[Compare Total Expenses with Budget]
    N --> O{Are Expenses Within Budget?}
    O -- Yes --> P[Display Budget Surplus]
    O -- No --> Q[Calculate Budget Shortfall]
    P --> R[Identify Largest Expense Category]
    Q --> R
    R --> S[Generate Travel Budget Report]
    S --> T[/Display Converted Expenses, Fees, Total Spending, Budget Status and Largest Category/]
    T --> U([Stop])
```
 
