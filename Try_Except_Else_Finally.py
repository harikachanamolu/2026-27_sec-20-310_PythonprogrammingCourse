try:
    text = input("Enter a number: ")
    num = int(text)

except ValueError:
    print("Error: Please enter a valid integer.")

else:
    print("Square:", num ** 2)

finally:
    print("Program finished")