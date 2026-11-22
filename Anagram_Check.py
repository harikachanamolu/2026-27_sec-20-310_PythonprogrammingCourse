# Get two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check whether the strings are anagrams
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")