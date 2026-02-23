#Problem Statement - Crate a program to find the maximum of 3 numbers.
no1 = float(input("Enter the first number: "))
no2 = float(input("Enter the second number: "))
no3 = float(input("Enter the third number: "))
if no1 >= no2 and no1>= no3 :
    print(f"The maximum number is: {no1}")
elif no2 >= no1 and no2 >= no3:
    print(f"The maximum number is: {no2}")
else:
    print(f"The maximum number is: {no3}")
