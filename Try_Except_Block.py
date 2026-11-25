try:
    result = 10 / 0
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")