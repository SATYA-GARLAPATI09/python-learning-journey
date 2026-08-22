# 11. Write a program to perform the given operations on a list:  
# i. Addition      ii. Insertion  iii. slicing 
length = int(input("enter the length of the list: "))
list=[]
for i in range(length):
    num = int(input("enter the num: "))
    list.append(num)

print("Original list:", list)

# i. Addition
new_element = int(input("enter the element to add: "))
list.append(new_element)
print("List after addition:", list)

# ii. Insertion
index = int(input("enter the index where you want to insert: "))
element = int(input("enter the element to insert: "))
list.insert(index, element)
print("List after insertion:", list)

# iii. Slicing
start = int(input("enter the start index for slicing: "))
end = int(input("enter the end index for slicing: "))
sliced_list = list[start:end]
print("Sliced list:", sliced_list)