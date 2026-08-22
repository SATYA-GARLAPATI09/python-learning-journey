# 9. Write a program to find the length of the string without using any library functions. 
str = input("Enter a string: ")
def find_length(s):
    count = 0
    for char in s:
        count += 1
    return count

print(find_length(str))