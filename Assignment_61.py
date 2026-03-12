#Problem statement : Write a function greet user that takes a user’s name as a parameter and prints a personalized 
#greeting message. 

def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python programming world!")
user_name = input("Please enter your name: ")
greet_user(user_name)
