#wap take two no from keyboard enter your choice 1.add 2.sub 3.mult 4.division




print("Enter two numbers:")
a = int(input())
b = int(input())

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Addition =", a + b)
    case 2:
        print("Subtraction =", a - b)
    case 3:
        print("Multiplication =", a * b)
    case 4:
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid choice")



"""print("Enter two numbers")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult ")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("sum=",no1+no2)
    case 2:
        print("sub=",no1-no2)
    case 3:
        print("mult=",no1*no2)
    case _:
        print("Invalid choice")"""



"""print("enter two number ")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult ")
ch=int(input())
match ch:
    case 1:print("sum=",no1+no2)
    case 2:print("sub=",no1-no2)
    case 3:print("mult=",no1*no2)
    case _:print("invalid choice ")"""



