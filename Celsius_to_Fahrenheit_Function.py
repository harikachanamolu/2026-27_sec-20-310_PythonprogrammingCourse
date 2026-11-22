# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Call the function
result = celsius_to_fahrenheit(celsius)

# Display the result
print("Temperature in Fahrenheit:", result)