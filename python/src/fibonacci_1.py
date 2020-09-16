# Use recursion
def fibonacci_1(n):
	if (n<0):
		print("Incorrect input")
	elif (n==1):
		return 0
	elif (n==2):
		return 1
	else:
		return fibonacci_1(n-1) + fibonacci_1(n-2)
		
print(fibonacci_1(9))