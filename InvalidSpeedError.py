class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter vehicle speed (km/h): "))

    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120 km/h")

    print("Valid vehicle speed:", speed, "km/h")

except InvalidSpeedError as e:
    print("Invalid Speed Error:", e)

except ValueError:
    print("Please enter a valid number.")