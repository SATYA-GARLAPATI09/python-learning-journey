# 12. Write a program to perform any 5 built-in functions by taking any list. 

length = int(input("enter the length of the list: "))
list=[]
for i in range(length):
    num = int(input("enter the num: "))
    list.append(num)

print("Original list:", list)

# 1. len() - Get the length of the list
print(f"the length of the list: {len(list)}")

# 2. reverse() - Reverse the list
list.reverse()
print("List after reversing:", list)

# 3. sort() - Sort the list in ascending order
list.sort()
print("List after sorting:", list)

# index() - Get the index of an element in the list
element = int(input("enter the element to find its index: "))

print(f"Index of {element}: {list.index(element)}")


# 5. count() - Count the occurrences of an element in the list
element = int(input("enter the element to count its occurrences: "))    
print(f"Occurrences of {element}: {list.count(element)}")

