# Read dimension
n = int(input("dimension: "))

# Read first matrix
print("first matrix:")
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

# Read second matrix
print("second matrix:")
B = []
for i in range(n):
    B.append(list(map(int, input().split())))

# Initialize result matrix
result = [[0] * n for _ in range(n)]

# Matrix multiplication
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]

# Print result (no trailing spaces)
print("Resultant Matrix:")
for row in result:
    print(*row)
