#Return value with argument





def fact(n):
	f=1
	while n>0:
		f=f*n
		n=n-1
	return f
print("Enter a number")
n=int(input())
res=fact(n)
print("Factorial=",res)