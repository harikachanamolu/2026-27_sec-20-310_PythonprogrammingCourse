a=int(input("enter a first number"))
b=int(input("enter a second number"))
print("addition=",a+b)
print("subtraction=",a-b)
print("multiplication=",a*b)
if b!=0:
    print("division=",a/b)
    print("floor division=",a//b)
    print("modulus=",a%b)
else:
    print("division is not possible")
    print("floor division is not possible")
    print("modulus s not possible")
print("exponentiation=",a**b)