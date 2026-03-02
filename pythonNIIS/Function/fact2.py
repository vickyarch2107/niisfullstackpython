#Return value without argument





def fact():
	print("Enter a number")
	n=int(input())
	f=1
	while n>0:
		f=f*n
		n=n-1
	return f
res=fact()
print("Factorial=",res)