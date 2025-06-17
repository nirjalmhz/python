
# Divisible by 400 → Leap year

# Divisible by 4 but not by 100 → Leap year

# Else → Not leap year
year=int(input("Enter the year to check whether it is leap year or not"))
if year%400==0:
    print("Its a leap year")
elif(year%4==0 and year%100!=0):
    print("Its a leap year")
else:
    print("Its not a leap year")