#Problem Statement: Create a program to insert and remove elements from a dictionary.
dict ={
    "name" : "Kunal",
    "Age" : 22,
    "City" : "Pune",
    "Education" : "B.Tech",
    "Profession" : "Student"
}
# Inserting an element
dict["Hobby"] = "Coding"   
print("After Inserting an element: ", dict)
# Removing an element
del dict["City"]
print("After Removing an element: ", dict) 
