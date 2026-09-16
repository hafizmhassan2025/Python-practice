def factorial(num):
  if num>0:
    return num * factorial(num-1)
  else:
    return 1

number = int(input("Enter the number: ")
result = factorial(number)
print("The factoiral of the number is: ",result)
