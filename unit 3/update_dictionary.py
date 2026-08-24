# 16. Write a program to add a new key-value pair to an existing dictionary. 
Student = {
    "name": "satya",
    "rollno": 123,
    "branch": "CSE",
}
print(f"before update the dictionary: {Student}")

Student["marks"] = 90
print(f"after update the dictionary: {Student}")