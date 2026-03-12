#Problem statement : Create a program to find a factorial of number using recursion.


def fact(n):
    if n == 0 or n == 1 :
        return 1 
    return fact(n - 1)*n

n = int(input("Enter a number to find its factorial: "))
print  (fact(n))
