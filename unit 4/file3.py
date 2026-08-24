# 20. Python program to compute the number of characters, words and lines in a file. 
file_content = input("Enter the content for the file: ")

f = open("source3.txt", "w")
f.write(file_content)
f.close()

f = open("source3.txt", "r")
content = f.read()
f.close()

char_count = len(content)
word_count = len(content.split())
line_count = content.count('\n') + 1

print(f"Number of characters: {char_count}")
print(f"Number of words: {word_count}")
print(f"Number of lines: {line_count}")