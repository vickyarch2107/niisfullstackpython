#No return value no argument



def check():
	print("Enter a number")
	no=int(input())
	print("Even number") if no%2==0 else print("Odd number")
check()