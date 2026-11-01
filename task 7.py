
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
