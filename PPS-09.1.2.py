# Type your code here...
def check_pal(s):
	if s==s[::-1]:
		print("Palindrome")
	else :
		print("Not a Palindrome")
s1=input()
check_pal(s1)
