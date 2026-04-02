'''
153=1**3+5**3+3**3=153  armstrong
12=1**2+2**2=5          not armstrong
hence power = no of digits
'''

no=int(input("Enter a number"))
p=0
temp=no
while temp!=0:
	temp=temp//10
	p=p+1
temp=no
arm=0
while temp!=0:
	r=temp%10
	arm=arm+r**p
	temp=temp//10 
if no==arm:
	print(no,"Is armstrong number")

'''
s=int(input("Enter start value"))
n=int(input("Enter a range:"))
for no in range(s,n+1):
	p=0
	temp=no
	while temp!=0:
		temp=temp//10
		p=p+1
	temp=no
	arm=0
	while temp!=0:
		r=temp%10
		arm=arm+r**p
		temp=temp//10 
	if no==arm:
		print(no,"Is armstrong number")
'''


