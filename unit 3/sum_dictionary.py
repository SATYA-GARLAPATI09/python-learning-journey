# 17. Write a program to sum all the items in a given dictionary.  
Student ={
    "rollno": 123,  
    "marks": 90,
    "cgpa": 9.5
}


sum_values = sum(Student.values())
print(f"The sum of all items in the dictionary is: {sum_values}")