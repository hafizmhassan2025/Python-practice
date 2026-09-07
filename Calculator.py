number_1 = int(input("Enter the 1st number:  "))
number_2 = int(input("Enter the 2nd number:  "))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
operator = int(input("Enter the operator number"))

if operator==1:
    print(f"Addition of {number_1} and {number_2} is ", number_1+number_2)
elif operator==2:
    print(f"Differnce of {number_1} and {number_2} is ", number_1-number_2)
elif operator==3:
    print(f"Multiplication of {number_1} and {number_2} is ", number_1*number_2)
elif operator==4:
    print(f"Division of {number_1} and {number_2} is ", number_1/number_2)
else:
    print("You entered wrong operator number")