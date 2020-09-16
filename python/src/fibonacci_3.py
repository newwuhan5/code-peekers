# Use dynamic programming
g=10
def fibonacci_3(n):
	a=0
	b=1
	if (n<0):
		print("Incorrect input")
	elif (n==1):
		return a
	elif (n==2):
		return b
	else:
		for i in range(2, n):
			c=a+b
			a=b
			b=c
			#f=10
			#e=10
			#g=e+f
			#print(g)
			#print(f)
		return c # b
		
print(fibonacci_3(9))