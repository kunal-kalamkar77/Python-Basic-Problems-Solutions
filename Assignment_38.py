#Problem Statement - Program to Remove the Duplicate Items from a List 
list = input("Enter the list of items separated by space: ").split()
unique_list = []
for item in list:
    if item not in unique_list:
        unique_list.append(item)
print("The list of unique items is: ", unique_list)
sorted_list = sorted(unique_list)
print("The sorted list of unique items is: ", sorted_list)
