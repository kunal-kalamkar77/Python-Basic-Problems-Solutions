#Problem statement - Create a program to check if given list is empty or not.
list = input("Enter a list : ").split()
if len(list) == 0:
    print("The list is empty.")
else:
    print("The list is not empty.")
    print("The list is : ", list)
