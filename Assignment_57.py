#Problem Statement : Create a funtion with default argument.

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
name_input = input("Enter your name: ")
print(greet(name_input))
