numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter a list index: "))
    print("Element:", numbers[index])

except ValueError:
    print("Error: Please enter a valid integer.")

except IndexError:
    print("Error: List index is out of range.")