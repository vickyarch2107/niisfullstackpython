#Return value without argument



def sical():
	print("Enter principle:")
	p=float(input())
	print("Enter rate of intrest:")
	r=float(input())
	print("Enter time:")
	t=float(input())
	si=p*t*r/100
	return si
res=sical()
print("Simple Intrest=", res)
