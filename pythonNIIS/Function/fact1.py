#No return value with argument




def fact(n):
	f=1
	while n>0:
		f=f*n
		n=n-1
	print("Factorial=",f)
print("Enter a number")
n=int(input())
fact(n)