"""WAP take emp salary from keyboard if sal>=5000 da=30%, hra=20% and if sal<5000 da=20%, hra=10% then
display basicsalary da hra and total salary."""




print("Enter basic salary")
sal=float(input())
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
else:
	da=sal*0.2
	hra=sal*0.1
ts=sal+da+hra
print("Basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("Total salary=",ts)


"""print("Enter basic salary")
sal=float(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
ts=sal+da+hra
print("Basic salary=",sal)
print("Da=",da)
print("Hra=",hra)
print("Total salary=",ts)"""
