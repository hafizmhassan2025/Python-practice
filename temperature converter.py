print("Enter your choice")
choice = int(input("1. Celsius to Fahrenheit\n2.Fahrenheit to Celsius"))

if choice == 1:
    celsius =float(input("Enter the temperature in Celsius"))
    fahrenheit = (celsius*(9/5)+32)
    print(f"Temperature in Celsius{celsius}\nTemperature in Fahrenheit{fahrenheit}")
elif choice ==2:
    fahrenheit = float(input("Enter the temperature in Fahrenheit"))
    calsius = (fahrenheit*(5/9)-32)
    print(f"Temperature in Fahrenheit{fahrenheit}\nTemperature in Celsius{calsius}")
else:
    print("You entered wrong choice")

