# Create an empty list
my_list = []

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Read list elements
for i in range(n):
    num = int(input("Enter a number: "))
    my_list.append(num)

# Find largest and smallest elements
largest = max(my_list)
smallest = min(my_list)

# Display the results
print("List:", my_list)
print("Largest element:", largest)
print("Smallest element:", smallest)