# 14. Write a program to count the number of vowels in a string (No control flow allowed). 

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count}")