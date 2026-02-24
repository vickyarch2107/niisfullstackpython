#WAP two nos from keyboard enter your choice 1.add 2.sub 3.mul invalid choice(menu driven program)



print("Enter two nos")
no1=int(input())
no2=int(input())
print("Enter your choice\n1.add\n2.sub\n3.mul")
ch=int(input())
if ch==1:
	print("Sum=",no1+no2)
elif ch==2:
	print("Sub=",no1-no2)
elif ch==3:
	print("Mul=",no1*no2)
else:
	print("Invalid choice")




#match case.......
"""print("Enter two nos")
no1=int(input())
no2=int(input())
print("Enter your choice\n1.add\n2.sub\n3.mul")
ch=int(input())
match ch:
	case 1:print("Sum=",no1+no2)
	case 2:print("Sub=",no1-no2)
	case 3:print("mul=",no1*no2)
	case _:print("Invalid choice")"""    #'_'is use for default case.

	