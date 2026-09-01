# Print the number from 1 to 50
# Print Fizz if the number is multiple of 3
# Print Buzz if the number is multiple of 5
# Print FizzBuzz if the number is multiple of both

start = int(input("Enter the number from where to start")
end = int(intput("Enter the number where to stop")
          
for i in range(start,end):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        print(i)                
