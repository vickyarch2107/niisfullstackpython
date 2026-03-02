#No return value with argument



def check(n):
	print("Even number") if n%2==0 else print("Odd number")
n=int(input("Enter a number:\n"))
check(n)