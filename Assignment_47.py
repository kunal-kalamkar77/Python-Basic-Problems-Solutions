#Problem Statement :Program to merge two Python dictionaries.
dict1 = {
    "name": "Kunal",
    "Age": 22,
    "City": "Pune"
}
dict2 = {
    "Education": "B.Tech",
    "Profession": "Student"
}
# Merging dictionaries
dict1.update(dict2)
print("Merged Dictionary:", dict1)
