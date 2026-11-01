
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
    Algorithm
1. Start the program.
2. Enter the total travel budget in Indian Rupees.
3. Enter the number of travel expenses.
4. For each expense, enter the category, amount, and exchange rate.
5. Convert the foreign currency amount into Indian Rupees.
6. Calculate a 2% currency conversion fee.
7. Add the conversion fee to the converted amount.
8. Calculate the total travel expenses.
9. Identify the category with the highest expense.
10. Compare total expenses with the planned budget.
11. Display whether the budget is within the limit or exceeded.
12. Display the largest expense category and its amount.
13. Stop the program.
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
START

INPUT total travel budget in INR
INPUT number of expenses

SET total_expenses = 0
SET largest_expense = 0
SET largest_category = ""

FOR each expense

    INPUT expense category
    INPUT expense amount
    INPUT foreign currency exchange rate

    CONVERT expense into INR
        converted_amount = expense_amount * exchange_rate

    CALCULATE conversion fee
        fee = converted_amount * 2 / 100

    CALCULATE total expense
        final_amount = converted_amount + fee

    ADD final_amount to total_expenses

    IF final_amount > largest_expense THEN
        largest_expense = final_amount
        largest_category = expense category
    END IF

END FOR

DISPLAY total_expenses

IF total_expenses <= budget THEN
    DISPLAY "Within Budget"
ELSE
    DISPLAY "Budget Exceeded"
END IF

DISPLAY largest_category
DISPLAY largest_expense

STOP
====== MULTI-CURRENCY TRAVEL BUDGET ======

Enter travel budget in INR: 100000
Enter number of expenses: 3

Expense 1:
Enter category: Hotel
Enter amount in USD: 300
Enter exchange rate: 84

Converted Amount: Rs. 25200
Conversion Fee (2%): Rs. 504
Total Expense: Rs. 25704

Expense 2:
Enter category: Food
Enter amount in EUR: 150
Enter exchange rate: 92

Converted Amount: Rs. 13800
Conversion Fee (2%): Rs. 276
Total Expense: Rs. 14076

Expense 3:
Enter category: Shopping
Enter amount in GBP: 200
Enter exchange rate: 108

Converted Amount: Rs. 21600
Conversion Fee (2%): Rs. 432
Total Expense: Rs. 22032

------------------------------------
          TRAVEL BUDGET REPORT
------------------------------------

Travel Budget: Rs. 100000
Total Expenses: Rs. 61812
Remaining Budget: Rs. 38188

Budget Status: Within Budget

Largest Expense Category: Hotel
Largest Expense: Rs. 25704

------------------------------------
Thank you!
The Multi-Currency Travel Budget Analysis system converts foreign currency expenses into Indian Rupees using supplied exchange rates. It calculates conversion fees, finds the total travel expenses, and compares them with the planned budget. It also identifies the largest expense category. This system helps travellers manage their expenses, control their budget, and plan their trips efficiently.
 
