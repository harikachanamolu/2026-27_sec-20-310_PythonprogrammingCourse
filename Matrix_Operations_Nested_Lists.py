# Creating two matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Display matrices
print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

# Matrix Addition
addition = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        addition[i][j] = A[i][j] + B[i][j]

print("Matrix Addition:")
for row in addition:
    print(row)

# Matrix Subtraction
subtraction = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        subtraction[i][j] = A[i][j] - B[i][j]

print("Matrix Subtraction:")
for row in subtraction:
    print(row)

# Matrix Multiplication
multiplication = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            multiplication[i][j] += A[i][k] * B[k][j]

print("Matrix Multiplication:")
for row in multiplication:
    print(row)