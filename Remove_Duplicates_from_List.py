# Create a list
my_list = [10, 20, 30, 20, 40, 10, 50]

print("Original List:", my_list)

# Remove duplicate elements
new_list = []

for item in my_list:
    if item not in new_list:
        new_list.append(item)

# Display the result
print("List after removing duplicates:", new_list)