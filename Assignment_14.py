#Problem Statment - Create a program to check if given date is valid or not.
date = input("Enter a date (dd/mm/yyyy) : ")
d, m, y = map(int, date.split('/'))
if m in [1, 3, 5, 7, 8, 10, 12]:
    if d >= 1 and d <= 31:
        print(date, "is a valid date.")
    else:
        print(date, "is not a valid date.")
elif m in [4, 6, 9, 11]:
    if d >= 1 and d <= 30:
        print(date, "is a valid date.")
    else:
        print(date, "is not a valid date.")
elif m == 2 :
    if y % 4 == 0:
        if d >= 1 and d <= 29:
            print(date, "is a valid date.")
        else:
            print(date, "is not a valid date.")
    else:
        if d >= 1 and d <= 28:
            print(date, "is a valid date.")
        else:
            print(date, "is not a valid date.")
