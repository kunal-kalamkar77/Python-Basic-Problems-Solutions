#Problem Statement: Create a program to check whether a given key already exists in a dictionary. 
dict = {
    "name": "Kunal",
    "Age": 22,
    "City": "Pune",
    "Education": "B.Tech",
    "Profession": "Student"
}
key_to_check = input("Enter the key to check: ")
if key_to_check in dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
