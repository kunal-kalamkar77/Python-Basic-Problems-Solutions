#Problem Statement - Create a program to find the second largest number in a list.
list = input("Enter a list of numbers : ").split()
largest = max(list)
list.remove(largest)
second_largest = max(list)
print("The second largest number in the list is: ", second_largest)
