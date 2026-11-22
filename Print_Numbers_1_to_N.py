n = int(input("Enter a number: "))

print("Numbers from 1 to", n, "are:")

for i in range(1, n + 1):
    print(i)

    n = int(input("Enter a number: "))

print("Numbers from 1 to", n, "are:")

i = 1
while i <= n:
    print(i)
    i = i + 1