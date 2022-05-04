# python program to find scholarship for based on marks

marks = int(input("Enter your score: "))

def scholarship(m):
	if m == 1100:
		print("Free education.")
	elif m > 1000:
		print("80% monthly fees deduction.")
	elif m > 900:
		print("60% monthly fees deduction.")
	elif m > 800:
		print("40% monthly fees deduction.")
	elif m > 700:
		print("30% monthly fees deduction.")
	elif m > 600:
		print("No scholarship")
	else:
		print("Invalid mark")

scholarship(marks)