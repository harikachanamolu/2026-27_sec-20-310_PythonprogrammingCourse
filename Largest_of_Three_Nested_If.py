a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b:
    if a>=c:
        print("largest number is:",a)
    else:
        print("largest number is:",c)
else:
    if b>=c:
        print("largest nuber is:",b)
    else:
        print("largest number is:",c)