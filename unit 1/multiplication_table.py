num = int(input("enter the number: "))
num_2 = int(input("enter the table end: "))
total =0
print(f"Multiplication table of {num} is:")
for i in range(1, num_2 + 1):
    total = num *i
    print(f"{num} * {i} = {total}")