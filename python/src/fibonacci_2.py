# Use dynamic programming
fibArray = [0, 1]
def fibonacci_2(n):
	if (n<0):
		print("Incorrect input")
	elif (n<=len(fibArray)):
		return fibArray[n-1]
	else:
		temp = fibonacci_2(n-1) + fibonacci_2(n-2)
		fibArray.append(temp);
		return temp
		
print(fibonacci_2(9))