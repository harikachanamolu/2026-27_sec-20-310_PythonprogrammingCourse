
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
Algorithm
1. Start the program.
2. Enter the number of products.
3. Enter each product's name, quantity, price, and category.
4. Calculate the product amount by multiplying quantity and price.
5. Apply tax according to the product category:
   - Food – 5%
   - Clothing – 8%
   - Electronics – 18%
6. Calculate the total subtotal and tax.
7. Apply discounts based on the subtotal:
   - ₹2,000 or above – 5%
   - ₹5,000 or above – 10%
   - ₹10,000 or above – 20%
8. Check that the discount does not exceed ₹2,000.
9. Calculate the final bill by adding tax and subtracting the discount.
10. Display the itemized invoice.
11. Stop the program.
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
START

INPUT number of products
SET subtotal = 0
SET total_tax = 0

FOR each product:
    INPUT product name
    INPUT quantity
    INPUT price per unit
    INPUT product category

    CALCULATE amount = quantity × price per unit

    IF category is Food:
        tax_rate = 5%
    ELSE IF category is Clothing:
        tax_rate = 8%
    ELSE IF category is Electronics:
        tax_rate = 18%
    ELSE:
        DISPLAY "Invalid category"
        CONTINUE

    CALCULATE tax = amount × tax_rate / 100
    CALCULATE product_total = amount + tax

    ADD amount to subtotal
    ADD tax to total_tax

    DISPLAY product details

END FOR

IF subtotal >= 10000:
    discount_rate = 20%
ELSE IF subtotal >= 5000:
    discount_rate = 10%
ELSE IF subtotal >= 2000:
    discount_rate = 5%
ELSE:
    discount_rate = 0%

CALCULATE discount = subtotal × discount_rate / 100

IF discount > 2000:
    discount = 2000

CALCULATE final_bill = subtotal + total_tax - discount

DISPLAY itemized invoice
DISPLAY subtotal, total tax, discount, final bill

STOP
    
 ========== RETAIL BILLING SYSTEM ==========

Enter number of products: 3

Product 1:
Enter product name: Rice
Enter category: Food
Enter quantity: 2
Enter price per item: 500
Tax rate: 5%
Amount: Rs. 1000
Tax: Rs. 50

Product 2:
Enter product name: Shirt
Enter category: Clothing
Enter quantity: 2
Enter price per item: 1000
Tax rate: 8%
Amount: Rs. 2000
Tax: Rs. 160

Product 3:
Enter product name: Headphones
Enter category: Electronics
Enter quantity: 1
Enter price per item: 3000
Tax rate: 18%
Amount: Rs. 3000
Tax: Rs. 540

-------------------------------------------
             ITEMIZED INVOICE
-------------------------------------------
Product       Amount       Tax
Rice          Rs.1000      Rs.50
Shirt         Rs.2000      Rs.160
Headphones    Rs.3000      Rs.540

Subtotal:              Rs.6000
Total Tax:             Rs.750
Amount Before Discount: Rs.6750
Discount:               Rs.675
Maximum Discount:       Rs.2000
Final Bill Amount:      Rs.6075
-------------------------------------------

Thank you for shopping!
The Retail Billing System calculates the total cost of multiple products based on their quantities and category-specific taxes. It applies discounts according to purchase amount thresholds and ensures that the discount does not exceed the maximum concession limit. Finally, it generates an itemized invoice showing the subtotal, tax, discount, and final bill amount. This system makes the billing process simple, accurate, and efficient.
