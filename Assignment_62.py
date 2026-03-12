#Problem Statement : Given a sequence of integers that end with a 00. Print the sequence in reverse  
#order. Don't use lists or other data structures. Use the force of recursion instead. 

def reverse_sequence():
    num = input("Enter an integer (or '00' to stop): ")
    if num == "00":
        return
    reverse_sequence()
    print(num)

print("Enter a sequence of integers (end with '00'):")
reverse_sequence()
