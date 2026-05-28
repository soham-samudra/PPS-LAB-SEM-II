# Read input
s = input()

# Keep only letters, digits, and spaces
result = ""

for ch in s:
    if ch.isalnum() or ch == " ":
        result += ch

# Print result
print(result)
