# Global bank balance
balance = 1000

# Function to deposit money
def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited:", amount)
    print("Updated Account Balance:", balance)

# Function using a local balance
def show_local_balance():
    balance = 500
    print("Local Balance:", balance)

# Display original balance
print("Original Account Balance:", balance)

# Deposit money
deposit(500)

# Call function with local variable
show_local_balance()

# Display actual account balance
print("Final Account Balance:", balance)