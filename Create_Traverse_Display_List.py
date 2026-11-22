# Create an empty list
my_list = []

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Insert elements into the list
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)

# Display the list
print("List elements:", my_list)

# Traverse the list
print("Traversing the list:")

for item in my_list:
    print(item)