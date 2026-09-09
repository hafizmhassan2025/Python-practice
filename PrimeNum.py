number = int(input("Enter the number\nThe number must be greater than zero.\n"))
Is_prime=True

if number < 2:
     Is_prime = False
else:
    for i in range(2,number):
        if number%i==0:
            Is_prime = False
            break
           
if Is_prime:
     print("The number is prime.")
else:
     print("The number is non-prime.")
    