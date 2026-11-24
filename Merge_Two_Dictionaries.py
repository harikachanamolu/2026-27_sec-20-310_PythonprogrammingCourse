# Create two dictionaries
dict1 = {"Python": 90, "Java": 85}
dict2 = {"HTML": 80, "CSS": 88}

# Create a copy of the first dictionary
merged_dict = dict1.copy()

# Merge the second dictionary using update()
merged_dict.update(dict2)

# Display the dictionaries
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)