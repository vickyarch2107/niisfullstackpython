#No return value no argument



def fact():
	print("Enter a number")
	n=int(input())
	f=1
	while n>0:
		f=f*n
		n=n-1
	print("Factorial=",f)
fact()



#0!=1
#1!=1
#-ve value have no factorial