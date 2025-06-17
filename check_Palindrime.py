pal=(input("Enter number to check the Palindrome:"))
copy_Palindrome=pal[::-1]
if pal==copy_Palindrome:
    print("Its Palindrome.")
elif pal=="0":
    print("Its zero")
else:
    print("Its not Palindrome")
 