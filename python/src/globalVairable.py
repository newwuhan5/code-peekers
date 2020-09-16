a=2
def add():
	global a
	b=3
	c=a+b
	print(c)
	
add() # 5

print(a) # 2

print(c) # Traceback (most recent call last):
#  File "C:\dev\python\globalVairable.py", line 10, in <module>
#    print(c)
# NameError: name 'c' is not defined