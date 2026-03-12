#Problem Statement :Create a function named count vowels that accepts a string and returns the number of vowels in the string. 

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
input_string = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(input_string)}.")
