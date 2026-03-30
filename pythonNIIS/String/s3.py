'''WAP take string from keyboard count no of char, no of alp, no of uppercase, no of lowercase, no of vowel,
 no of conconect, no of digit, no of spaces and symbols, no of words'''






s=input("Enter a string:")
c,alp,up,lw,vw,co,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i  in s:
	c+=1
	if i.isalpha():
		alp=alp+1
		if i.isupper():
			up+=1
		else:
			lw+=1
			if i in "aeiouAEIOU":
				vw+=1
			else:
				co+=1
	elif i.isdigit():
		dg+=1
	elif i.isspace():
		sp+=1
	else:
		sy+=1
wd=sp+1
print("no of char=",c)
print("no of alp=",alp)
print("no of up=",up)
print("no of lw=",lw)
print("no of co=",co)
print("no of dg=",dg)
print("no of sp=",sp)
print("no of sy=",sy) 
print("no of wd=",wd)	


