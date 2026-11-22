# Global variable
x = 100

# Define a function
def display():
    # Local variable
    x = 50
    print("Local variable x:", x)

# Call the function
display()

# Display global variable
print("Global variable x:", x)