def check(num):
	if num <= 9:
		print("Single Digit")
	elif num >9 and num <=99:
		print("Double Digit")
	else:
		print("Others")

if __name__ == "__main__":
	num = int(input("Input a number:"))
	check(num)