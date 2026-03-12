#Problem statement : CReate a program to check if a given number is even or odd.


def check(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter a number: "))
result = check(n)
print(f"The number {n} is {result}.")  
