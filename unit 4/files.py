# Write a program to sort words in a file and put them in another file. The output file should have 
# only lower-case words, so any upper-case words from source must be lowered.
file1 = input("enter the text in file 1: ")
f=open("source.txt", "w")
f.write(file1)

f=open("source.txt", "r")
words = f.read().split()
lowercase_words = [word.lower() for word in words]
lowercase_words.sort()

f=open("output.txt", "w")
f.write(" ".join(lowercase_words))
f.close()

# print the sorted words in the output file
f=open("output.txt", "r")