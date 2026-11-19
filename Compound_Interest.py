P=float(input("Enter principle amount:"))
R=float(input("Enter rate of interest:"))
T=float(input("Enter time period in year:"))
a=P*(1+R/100)**T
ci=a-P
print("compound interest=",ci)
print("Total Amount=",a)