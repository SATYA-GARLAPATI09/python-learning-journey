# 15. Write a program to check if a given key exists in a dictionary or not.  

Student = {
"name": "satya",
"rollno": 123,
"branch": "CSE",
"marks": 90
}

key = input("Enter the key to check: ")

if key in Student:
    print(f"The key '{key}' exists in the dictionary.")

else:
    print(f"The key '{key}' does not exist in the dictionary.")