# 19. Python program to print each line of a file in reverse order.  
source_file = input("Enter the source file content: ")

f = open("source2.txt", "w")
f.write(source_file)    
f.close()


f=open("source2.txt", "r")
words = f.read().split()

# the line have to be reversed and written to the output file

f=open("output2.txt", "w")
f.write(" ".join(words[::-1]))
f.close()

f=open("output2.txt", "r")
print(f.read())
f.close()