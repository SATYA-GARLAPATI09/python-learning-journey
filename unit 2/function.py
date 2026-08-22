# 7. Write a program to define a function with multiple return values.  
def add_multiple(n1,n2):
    t = n1+n2
    total = n1*n2
    return t,total 
   



def multiple1(t,n2):
        t2 = t*n2
        return t2    


n1 = int(input("enter the num1: "))
n2 = int(input("enter the num2: "))
print("The sum of the two numbers is:", add_multiple(n1,n2))
print("the multiplication of the two numbers is :", multiple1(n1,n2))