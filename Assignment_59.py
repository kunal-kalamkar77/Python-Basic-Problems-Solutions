#Problem Statement : Create a program to find sum of the digit of a number recursively.

def sum_of_digits(n):
    if n == 0:
        return 0
    return sum_of_digits(n // 10) + (n % 10)
n = int(input("Enter a number to find the sum of its digits: "))
print(f"The sum of the digits of {n} is {sum_of_digits(n)}.")
