# Define a function with default rate = 5
def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Call function using default rate
si1 = simple_interest(10000, 2)
print("Simple Interest with default rate:", si1)

# Call function using explicit rate
si2 = simple_interest(10000, 2, 10)
print("Simple Interest with explicit rate:", si2)