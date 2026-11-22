# Define a function using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Call the function
print_details(name="Krishna", age=26, city="Guntur")