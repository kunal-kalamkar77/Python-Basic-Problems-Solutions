#Problem Statement : Create a function with keyword argument.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
name_input = input("Enter your name: ")
greeting_input = input("Enter a greeting (or press Enter for default): ")
if greeting_input:
    print(greet(name_input, greeting_input))
else:
    print(greet(name_input))
