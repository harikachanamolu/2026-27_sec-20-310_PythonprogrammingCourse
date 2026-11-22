n=int(input("Enter how many numbers:"))
largest=int(input("Enter number 1:"))
for i in range(2,n+1):
    num=int(input("Enter number:"))
    if num>largest:
        largest=num
        print("The largest number is:",largest)
