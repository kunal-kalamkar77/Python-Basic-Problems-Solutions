#Problem Statement : Program to Remove items from set1 that are not common to both set1 and set2 .
set1 = {1, 2, 3, 4, 5, 7, 9, 10}
set2 = {4, 5, 6, 7, 8, 10, 11, 12}
set3 = set1.intersection(set2)
if set3 == set1:
    print("All items in set1 are common to both sets.")
    print("The common items are:", set3)
else:
    set1.difference_update(set3)
    print("Items removed from set1 that are not common to both sets.")
    print("The common items are:", set3)
