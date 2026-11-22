# Get a string from the user
text = input("Enter a string: ")

# Reverse the string
reverse = text[::-1]

# Check palindrome
if text == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")