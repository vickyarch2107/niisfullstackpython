#WAP take a number from keyboard check no is sd dd td od +ve number check


print("Enter a number")
no=int(input())
if no>0:
	no=-no
if no<10:
	print("Single digit")
elif no<100:
	print("Double digit")
elif no<1000:
	print("Triple digit")
else:
	print("Other digit")
