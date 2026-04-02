a=0
b=1
r=int(input("enter a range:"))
print(a,b,end="\t")
while r>2:
	c=a+b
	print(c,end="\t")
	a=b
	b=c 
	r=r-1