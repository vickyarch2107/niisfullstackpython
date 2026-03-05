s=0
def sdtest(no):
	global s
	if no!=0:
		s=s+no%10
		no=no//10
		sdtest(no)
	return s
res=sdtest(125)
print("sumof dgit=",res)


"""def sum_of_digits(n):
    # Base case: when n is reduced to a single digit
    if n == 0:
        return 0
    else:
        # Recursive case: last digit + sum of remaining digits
        return (n % 10) + sum_of_digits(n // 10)

# Test the function
number = int(input("Enter a number: "))
print(f"The sum of the digits of {number} is: {sum_of_digits(number)}")"""