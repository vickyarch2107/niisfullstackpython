'''n=int(input("Enter a number:"))  #6,28
d=1
s=0
while d<=n//2:
	if n%d==0:
		s+=d 
	d=d+1
if s==n:
	print(n,"is perfect number")
else:
	print(n,"is not perfect number")'''





r=int(input("Enter a range:"))
for n in range(1,r+1):
	d=1
	s=0
	while d<=n//2:
		if n%d==0:
			s+=d 
		d=d+1
	if s==n:
		print(n,"is perfect number")
	













