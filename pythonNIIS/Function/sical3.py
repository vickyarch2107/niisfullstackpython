#Return value with argument



def sical(p,t,r):
	si=p*t*r/100
	return si
print("Enter principle:")
p=float(input())
print("Enter rate of intrest:")
r=float(input())
print("Enter time:")
t=float(input())
res=sical(p,t,r)
print("Simple Intrest=", res)
