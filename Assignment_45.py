#Problem Statement: Create a program to cocatenate dictionaries to create a new one.
dict1 = {
    "name": "Kunal",
    "Age": 22,
    "City": "Pune"
}
dict2 = {
    "Education": "B.Tech",
    "Profession": "Student"
}
# Concatenating dictionaries
new_dict = {**dict1, **dict2}
print("Concatenated Dictionary:", new_dict)
