number = int(input("Enter the number"))
factorial=1

if number==0:
    print("Factorial = 1")
elif number>0:
    for i in range(1,number+1):
        factorial=factorial*i
    print("Factorial =",factorial)
else:
    print("Undefined")        
    