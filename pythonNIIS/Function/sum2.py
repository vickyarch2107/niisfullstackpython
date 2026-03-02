#Return value without argument



def add():
	print("Enter 1st number:")
	no1=int(input())
	print("Enter 2nd number:")
	no2=int(input())
	s=no1+no2
	return s
res=add()
print("Sum=",res)
