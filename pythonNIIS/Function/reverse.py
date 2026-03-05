def reverse_number(n, rev=0):
    # Base case: when n becomes 0, return the reversed number
    if n == 0:
        return rev
    else:
        # Recursive case: shift current rev by 1 digit and add the last digit of n
        return reverse_number(n // 10, rev * 10 + n % 10)

# Test the function
number = int(input("Enter a number: "))
reversed_num = reverse_number(number)
print(f"The reverse of {number} is: {reversed_num}")