'''n=int(input("Enter a number:"))
d=2
c=0
while d<=n//2:
	if n%d==0:
		c=c+1
		break
	d=d+1 
if c==0:
	print(n,"Is prime no")
else:
	print(n,"Is not prime no")'''


'''s=int(input("Enter start value"))
n=int(input("Enter a range:"))
for n in range(s,n+1):
	d=2
	c=0
	while d<=n//2:
		if n%d==0:
			c=c+1
			break
		d=d+1 
	if c==0:
		s=s+n
		print(n,"Is prime no")'''


s=0
n=int(input("Enter a range:"))
for n in range(n//2,n+1):
	d=2
	c=0
	while d<=n//2:
		if n%d==0:
			c=c+1
			break
		d=d+1 
	if c==0:
		s=s+n
		print(n,"Is prime no")
print("Sum=",s)	







