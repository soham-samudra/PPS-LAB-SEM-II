marks = list(map(int, input().split()))
total = sum(marks)


percentage = total / 4


if percentage > 75:
	grade = "Distinction"
elif percentage >= 60:
	grade = "First Division"
elif percentage >= 50:
	grade = "Second Division"
elif percentage >= 40:
	grade = "Third Division"
else:
	grade = "Fail"


print(total)
print(f"{percentage:.2f}")
print(grade)

