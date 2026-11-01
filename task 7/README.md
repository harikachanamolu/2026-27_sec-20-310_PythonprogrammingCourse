
# Retail Billing with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ")
    price = float(input("Enter product price: Rs. "))
    quantity = int(input("Enter quantity: "))

    # Validate product details
    if price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    amount = price * quantity

    # Category-specific tax
    if category.lower() == "food":
        tax_rate = 5
    elif category.lower() == "clothing":
        tax_rate = 8
    elif category.lower() == "electronics":
        tax_rate = 18
    else:
        print("Invalid category!")
        continue

    tax = amount * tax_rate / 100

    subtotal += amount
    total_tax += tax

    print("\nProduct Name:", name)
    print("Category:", category)
    print("Quantity:", quantity)
    print("Price: Rs.", price)
    print("Amount: Rs.", amount)
    print("Tax:", tax_rate, "%")
    print("Tax Amount: Rs.", round(tax, 2))

# Calculate discount
print("\n===== DISCOUNT DETAILS =====")

if subtotal >= 10000:
    discount_rate = 20
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = 2000

if discount > max_discount:
    discount = max_discount

# Final bill
final_bill = subtotal + total_tax - discount

print("\n========== ITEMIZED INVOICE ==========")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("Discount Rate  :", discount_rate, "%")
print("Discount       : Rs.", round(discount, 2))
print("--------------------------------------")
print("Final Bill     : Rs.", round(final_bill, 2))
print("======================================")
print("Thank you for shopping!")
```mermaid
       
    flowchart TD
    A([Start]) --> B[/Enter Number of Products/]
    B --> C[/Enter Product Name, Category, Price and Quantity/]
    C --> D{Are Product Details Valid?}
    D -- No --> E[Display Invalid Product Details]
    E --> C
    D -- Yes --> F[Calculate Item Total]
    F --> G[Apply Category-Specific Tax]
    G --> H[Add Item Amount and Tax to Subtotal]
    H --> I{Are More Products Available?}
    I -- Yes --> C
    I -- No --> J[Calculate Total Subtotal]
    J --> K{Is Subtotal >= 10000?}
    K -- Yes --> L[Apply 20 Percent Discount]
    K -- No --> M{Is Subtotal >= 5000?}
    M -- Yes --> N[Apply 10 Percent Discount]
    M -- No --> O{Is Subtotal >= 2000?}
    O -- Yes --> P[Apply 5 Percent Discount]
    O -- No --> Q[No Discount]
    L --> R[Check Maximum Discount Limit of Rs. 2000]
    N --> R
    P --> R
    Q --> S[Calculate Final Discount]
    R --> S
    S --> T[Calculate Final Bill]
    T --> U[Generate Itemized Invoice]
    U --> V[/Display Products, Quantities, Taxes, Discount and Final Amount/]
    V --> W([Stop])
 ```
