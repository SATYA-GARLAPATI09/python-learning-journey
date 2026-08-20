#Write a program to find the largest element among three Numbers. 
#Here is a simple Python program to find the largest element among three numbers:

a=30
b= 40
c=60
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
print("The largest number is:", largest)