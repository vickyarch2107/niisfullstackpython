#Return value without argument



def check():
    n = int(input("Enter a number:\n"))
    if n % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

result = check()
print(result)