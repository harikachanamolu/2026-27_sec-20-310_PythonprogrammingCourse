# Declare a global counter
count = 0

# Define a function
def increment():
    global count
    count = count + 1
    print("Counter value:", count)

# Call the function multiple times
increment()
increment()
increment()
increment()
increment()