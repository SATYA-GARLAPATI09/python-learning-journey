# Write a Program to display all prime numbers within an interval  
list=[]
for i in range (1,201):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break


        else:
            list.append(i)  


print("The prime numbers in the interval are:",list)