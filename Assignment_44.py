#Problem Statement: Create a program to sort (ascending and descending) a dictionary by keys.
dict = {
    "name": "Kunal",
    "Age": 22,
    "City": "Pune",
    "Education": "B.Tech",
    "Profession": "Student"
}
# Sorting in ascending order
sorted_dict_asc = dict(sorted(dict.items()))
print("Ascending order:", sorted_dict_asc)
# Sorting in descending order
sorted_dict_desc = dict(sorted(dict.items(), reverse=True))
print("Descending order:", sorted_dict_desc)
