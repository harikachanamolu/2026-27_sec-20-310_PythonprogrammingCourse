rows = int(input("Enter the number of rows: "))
symbol = input("Enter the symbol (* or 0): ")

for i in range(1, rows + 1):
    for j in range(i):
        print(symbol, end=" ")
    print()