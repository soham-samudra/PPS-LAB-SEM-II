n = int(input().strip())

factorial = 1

# Loop from 1 to n
for i in range(1, n + 1):
    factorial *= i

print(factorial)
