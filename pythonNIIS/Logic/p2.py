'''
12344321
123  321
12    21
1      1
'''


c=0
for i in range(4,0,-1):                         
	for j in range(1,i+1,1):       
		print(j,end="")
	for j in range(0,c,1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	print()
	c+=2

#or


for i in range(4,0,-1):                         
	for j in range(1,i+1,1):       
		print(j,end="")
	for j in range(0,2*(4-i),1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	print()



'''
1      1
12    21
123  321
12344321
'''
for i in range(1,5,1):                         
	for j in range(1,i+1,1):       
		print(j,end="")
	for j in range(0,2*(4-i),1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	print()


'''
1
00
111
0000
'''
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print(i%2,end="")
	print()

'''
0
11
000
1111
'''
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print((i+1)%2,end="")
	print()


'''
0
10
101
1010
'''

for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print(j%2,end="")
	print()

'''
0
10
010
1010
'''
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print((i+j)%2,end="")
	print()


'''
1
01
101
0101
'''
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print((i+j+1)%2,end="")
	print()

'''
@
##
@@@
####
'''
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		if i%2==0:
			print("#",end="")
		else:
			print("@",end="")
	print()


'''
1
23
456
78910
'''
c=1
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print(c,end="")
		c+=1
	print()

'''
A
BC
DEF
GHIJ
'''
c=65
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print(chr(c),end="")
		c+=1
	print()


'''
1
3 2
4 5 6
10 9 8 7
'''
''' have to solve c=1
for i in range(1,5,1):                         
	for j in range(1,i+1,1):
		print(c,end=" ")
		c+=1
	print()'''



'''
ABCDDCBA
ABC  CBA
AB    BA
A      A
'''


c=0
for i in range(68,64,-1):                         
	for j in range(65,i+1,1):       
		print(chr(j),end="")
	for j in range(0,c,1):
		print(end=" ")
	for j in range(i,64,-1):
		print(chr(j),end="")
	print()
	c+=2


'''
n
ni
nii
niis
'''
s=input("Enter your name")
for i in range(0,len(s),1):
	for j in range(0,i+1,1):
		print(s[j],end="")
	print()


'''
niis
nii
ni
n
'''

s=input("Enter your name")
for i in range(len(s)-1,-1,-1):
	for j in range(0,i+1,1):
		print(s[j],end="")
	print()

'''
1598
159
15
1
'''

s="1598"
for i in range(len(s)-1,-1,-1):
	for j in range(0,i+1,1):
		print(s[j],end="")
	print()


'''
1
15
159
1598
'''	
s="1598"
for i in range(0,len(s),1):
	for j in range(0,i+1,1):
		print(s[j],end="")
	print()
