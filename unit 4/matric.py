# 22. Write a program to add, transpose and multiply two matrices.  
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

list3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Adding two matrices
for i in range(len(list1)):
    for j in range(len(list1[0])):
        list3[i][j] = list1[i][j] + list2[i][j]
        
print("Sum of the matrices:")
for row in list3:
    print(row)

# Transposing the first matrix
transpose1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(list1)):
    for j in range(len(list1[0])):
        transpose1[j][i] = list1[i][j]

print("Transpose of the first matrix:")
for row in transpose1:
    print(row)  

# Multiplying two matrices
product = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(list1)):
    for j in range(len(list2[0])):
        for k in range(len(list2)):
            product[i][j] += list1[i][k] * list2[k][j]  
            
print("Product of the matrices:")
for row in product:
    print(row)  