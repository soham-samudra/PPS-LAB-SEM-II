# Type Content here...
# Read input string
s = input().strip()

# Define vowels
vowels = "aeiouAEIOU"

count = 0

# Count vowels
for ch in s:
    if ch in vowels:
        count += 1

# Print result
print(count)
