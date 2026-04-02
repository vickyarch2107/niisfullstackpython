for i in range (1,5,1):               #11	
	for j in range(1,i+1,1):     	  #1221	
		print(j,end="") 			  #123321
	for i in range(i,0,-1):           #12344321
		print(j,end="")               #Error
	print()                       	  



for i in range (1,5,1):               #11	
	for j in range(1,i+1,1):     	  #1221	
		print(j,end="") 			  #123321
	for i in range(i,0,-1):           #12344321
		print(j,end="")				 #Error 
	print()                       	  
for i in range (4,0,-1):              	
	for j in range(1,i+1,1):     	  	
		print(j,end="") 			  
	for i in range(i,0,-1):       
		print(j,end="")
	print()                       	  


for i in range (4,0,-1):          #Error            	
	for j in range(1,i+1,1):     	  	
		print(j,end="") 			  
	for i in range(i,0,-1):       
		print(j,end="")
	print() 
for i in range (1,5,1):               #11	
	for j in range(1,i+1,1):     	  #1221	
		print(j,end="") 			  #123321
	for i in range(i,0,-1):           #12344321
		print(j,end="")				  
	print()



for i in range(4,0,-1):            #1234
	for j in range(4-i,0,-1):	   # 123
		print(end=" ")             #  12
	for j in range(1,i+1,1):       #   1
		print(j,end="")
	print()


for i in range(1,5,1):             #   1
	for j in range(4-i,0,-1):	   #  12
		print(end=" ")             # 123
	for j in range(1,i+1,1):       #1234
		print(j,end="")
	print()


for i in range(4,0,-1):            #1234321
	for j in range(4-i,0,-1):	   # 12321
		print(end=" ")             #  121
	for j in range(1,i+1,1):       #   1
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()


for i in range(1,5,1):             #   1
	for j in range(4-i,0,-1):	   #  121
		print(end=" ")             # 12321
	for j in range(1,i+1,1):       #1234321
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()


for i in range(4,0,-1):            #1234321
	for j in range(4-i,0,-1):	   # 12321
		print(end=" ")             #  121
	for j in range(1,i+1,1):       #   1
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()
for i in range(2,5,1):             
	for j in range(4-i,0,-1):	   #  121
		print(end=" ")             # 12321
	for j in range(1,i+1,1):       #1234321
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()


r=int(input("Enter a row"))
for i in range(r,0,-1):            
	for j in range(r-i,0,-1):	  
		print(end=" ")             
	for j in range(1,i+1,1):       
		print("*",end="")
	for j in range(i-1,0,-1):
		print("*",end="")
	print()
for i in range(2,r+1,1):             
	for j in range(r-i,0,-1):	   
		print(end=" ")             
	for j in range(1,i+1,1):       
		print("*",end="")
	for j in range(i-1,0,-1):
		print("*",end="")
	print()


r=int(input("Enter a row"))
for i in range(1,r+1,1):            
	for j in range(r-i,0,-1):	   
		print(end=" ")             
	for j in range(1,i+1,1):       
		print("*",end="")
	for j in range(i-1,0,-1):
		print("*",end="")
	print()
for i in range(r-1,0,1):             
	for j in range(r-i,0,-1):	   
		print(end=" ")             
	for j in range(1,i+1,1):       
		print("*",end="")
	for j in range(i-1,0,-1):
		print("*",end="")
	print()




