#Problem Statement - Create a program to find roots of a quadratic equation.
import math
a = float(input("Enter coefficient x^2 : "))
b = float(input("Enter coefficient x^1 : "))
c = float(input("Enter coefficient x^0 : "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real and different.")
    print("Root 1 : ", r1)
    print("Root 2 : ", r2)
elif d == 0:
    r = -b / (2*a)
    print("Roots are real and same.")
    print("Root : ", r)
else:
    print("Roots are complex and different.")
    real_part = -b / (2*a)
    imag_part = math.sqrt(-d) / (2*a)
    print("Root 1 : ", real_part, "+", imag_part, "i")
    print("Root 2 : ", real_part, "-", imag_part, "i")
