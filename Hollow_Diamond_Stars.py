n = int(input("Enter the number of rows: "))

# Upper half of the diamond
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half of the diamond
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()