def reverse_string(s):
	result=s[::-1] 
	return result

user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
