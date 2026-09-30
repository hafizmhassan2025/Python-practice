number=int(input("Enter the number"))
temp=number
rev=0

while temp>0:
    digit=temp%10
    rev=rev*10 +digit
    temp=temp//10
    
if number==rev:
    print(f"{number} is palindrome.")
else:
    print(f"{number} is not palindrome.")
    
