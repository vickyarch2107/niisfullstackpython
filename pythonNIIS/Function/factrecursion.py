"""factorial using function
def fact(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
res=fact(4)
print("factorial=",res)"""



#using recursion


f=1
def fact(no):
	global f
	if no>0:
		f=f*no
		no=no-1
		fact(no)
	return f
res=fact(4)
print("factorial=",res)

"""def fact(no):
	if no==0:
		return 1
	else:
		return no*fact(no-1)
res=fact(4)
print("factorial=",res)"""
