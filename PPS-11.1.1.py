num = int(input("Enter a number: "))

# Calculate sum of digits
digit_sum = 0
n = abs(num)  
while n > 0:
    digit_sum += n % 10
    n //= 10
print("Sum of digits:",digit_sum)
