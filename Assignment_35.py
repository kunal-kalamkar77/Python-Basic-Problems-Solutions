#Problem Statement - Create a program to put even and odd numbers in separate lists form given list.
list =  input("Enter a list of elemnets :").split()
even_list = []
odd_list = []
for i in list:
    if int(i) % 2 == 0:
        even_list.append(int(i))
    else:
        odd_list.append(int(i))
print("The even numbers in the list are: ", even_list)
print("The odd numbers in the list are: ", odd_list)
