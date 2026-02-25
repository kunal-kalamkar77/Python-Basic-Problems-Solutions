#Problem Statement: Program to check if two sets have any elements in common.
set1 = {1, 2, 3, 4, 5, 7, 9, 10}
set2 = {4, 5, 6, 7, 8, 10, 11, 12}
if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have some elements in common.", set1.intersection(set2))
