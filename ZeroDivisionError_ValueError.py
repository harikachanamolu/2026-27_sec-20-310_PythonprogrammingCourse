try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")