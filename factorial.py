number = int(input("Enter the number"))
factorial=1

if number==0 or number==1:
    print("Factorial = 1")
elif number>1:
    for i in range(1,number+1):
        factorial=factorial*i
    print("Factorial =",factorial)
else:
    print("Undefined")        
    