#Problem statement - program to swaptwo variables
#We will assign variables 1st
a = float(input("Enter any value :"))
b = float(input("Enter 2nd value :"))
temp = a
a = b
b = temp
print("Variables after swapping are :",(a,b))
