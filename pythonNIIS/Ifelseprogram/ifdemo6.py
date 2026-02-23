print("Enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
ts=sal+da+hra
print("Basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("Total salary=",ts)
