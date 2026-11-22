n=int(input("Enter a number:"))
temp=n
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
if n==reverse:
 print("palindrome number")
else:
   print("not a palindrome number")