class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter student marks (0-100): "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

except InvalidMarksError as e:
    print("Invalid Marks Error:", e)

except ValueError:
    print("Please enter a valid number.")

finally:
    print("Program finished.")