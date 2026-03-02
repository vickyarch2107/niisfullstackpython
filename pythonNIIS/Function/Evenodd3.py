#Return value with argument



def check(n):
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"
n = int(input("Enter a number:\n"))
res = check(n)
print(res)