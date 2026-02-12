#Problem statement - Create a program to find maximum of two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(f"The maximum of {num1} and {num2} is: {num1}")
elif num2 > num1:
    print(f"The maximum of {num1} and {num2} is: {num2}")
else:
    print(f"Both numbers are equal: {num1}")  
    
