for i in range (1,5,1):           #1
	for j in range (1,i+1,1):     #1	2   	
		print(j,end="\t")         #1	2	3
	print()                       #1	2	3	4


for i in range (1,5,1):           #1
	for j in range (1,i+1,1):     #2	2   	
		print(i,end="\t")         #3	3	3
	print()                       #4	4	4	4



for i in range (4,0,-1):          #1	2	3	4
	for j in range (1,i+1,1):     #1	2	3  	
		print(j,end="\t")         #1	2	
	print()                       #1	




for i in range (4,0,-1):          #4	4	4	4
	for j in range (1,i+1,1):     #3	3	3  	
		print(i,end="\t")         #2	2	
	print()                       #1	




for i in range (68,64,-1):        #A	B	C	D
	for j in range (65,i+1,1):    #A	B	C
		print(chr(j),end="\t")    #A	B	
	print()                       #A	


for i in range (65,69,1):         #A	
	for j in range (65,i+1,1):    #A	B	
		print(chr(j),end="\t")    #A	B	C
	print()                       #A	B	C	D	




for i in range (4,0,-1):          #4
	for j in range (4,i-1,-1):    #4	3  	
		print(j,end="\t")         #4 	3	2	
	print()                       #4 	3	2	1	


for i in range (1,5,1):           #4 	3	2	1
	for j in range (4,i-1,-1):    #4 	3	2 	
		print(j,end="\t")         #4 	3		
	print()                       #4 	



for i in range (65,69,1):           #D 	C 	B	A
	for j in range (68,i-1,-1):     #D 	C 	B	
		print(chr(j),end="\t")      #D 	C		
	print()                       	#D 	


for i in range (1,5,1):             #1
	for j in range (i,0,-1):     	#2	1	
		print(j,end="\t")      		#3	2	1		
	print()                       	#4 	3	2	1	



for i in range (4,0,-1):            #4 	3	2	1
	for j in range (i,0,-1):     	#3	2	1	
		print(j,end="\t")      		#2	1			
	print()                       	#1	



for i in range (4,0,-1):            #4	
	for j in range (i,5,1):     	#3	4	
		print(j,end="\t")      		#2	3	4		
	print()                       	#1	2	3	4




for i in range (68,64,-1):            #D	
	for j in range (i,69,1):     	  #C 	D	
		print(chr(j),end="\t")        #B 	C 	D		
	print()                       	  #A	B	C	D



for i in range (1,5,1):               #11	
	for j in range (1,i+1,1):     	  #121	
		print(j,end="")               #1231	
	print(1)                       	  #12341



