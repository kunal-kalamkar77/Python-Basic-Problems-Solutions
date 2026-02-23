#Problem Statement - Create a program to generate a list of 20 random numbers between 1 and 20, and append them to a list.
import random

list = []
for i in range(20):
    list.append(random.randint(1, 20))

print("The list of numbers is: ", list)
