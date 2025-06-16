print("Welcome to my Python Calculator ")
print("Select Operation you want to perform")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
print("6.Power")
operation=int(input("Enter Sn of the operation you want to enter"))
num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))
if operation==1:
    print("The sum of",num1,"and",num2,"is",num1+num2)
elif operation==2:
        print("The difference of",num1,"and",num2,"is",num1-num2)
elif operation==3:
          print("The product of",num1,"and",num2,"is",num1*num2)
elif operation==4:
            print("The division of",num1,"and",num2,"is",num1/num2)
elif operation==5:
        print("The remainder of",num1,"and",num2,"is",num1%num2)
elif operation==6:
            print("The power of",num1,"and",num2,"is",num1**num2)
else:
        print("Invalid option")

