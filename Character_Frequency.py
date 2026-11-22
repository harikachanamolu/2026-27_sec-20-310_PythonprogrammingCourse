# Get a string from the user
text = input("Enter a string: ")

# Create an empty dictionary
frequency = {}

# Count each character
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Display character frequency
print("Character Frequency:")

for ch, count in frequency.items():
    print(ch, ":", count)