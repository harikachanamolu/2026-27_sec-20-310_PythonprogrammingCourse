# Create a list with duplicate elements
my_list = [10, 20, 30, 20, 40, 10, 50, 30]

# Display the original list
print("Original List:", my_list)

# Convert list into a set to remove duplicates
unique_set = set(my_list)

# Convert set back into a list
unique_list = list(unique_set)

# Display the list without duplicates
print("List after removing duplicates:", unique_list)