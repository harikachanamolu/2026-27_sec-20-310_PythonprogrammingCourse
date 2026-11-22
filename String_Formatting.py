# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

# Using format() method
print("\nUsing format() method:")
print("My name is {}. I am {} years old.".format(name, age))

# Using f-string
print("\nUsing f-string:")
print(f"My name is {name}. I am {age} years old.")

# Using % operator
print("\nUsing % operator:")
print("My name is %s. I am %d years old." % (name, age))

# Formatting marks
print(f"My marks are {marks:.2f}")