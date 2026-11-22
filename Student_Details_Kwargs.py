# Define a function using **kwargs
def student_details(**kwargs):
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


# Call the function
student_details(
    name="Harika",
    Python=90,
    Maths=85,
    English=88
)