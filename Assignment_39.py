#Problem Statement: Create a program to create and view a dictionary.
data = {}
while True:
    key = input("Enter the key (or 'exit' to stop): ")
    if key == 'exit':
        break
    value = input(f"Enter the value for key '{key}': ")
    

    try:
        value = int(value)
    except ValueError:
        pass
    data[key] = value

print("Current Dictionary:", data)
