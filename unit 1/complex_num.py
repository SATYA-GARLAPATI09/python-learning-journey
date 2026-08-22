complex_num1 = 3 + 4j
complex_num2 = 1 - 2j

# Addition
def add_complex_numbers(c1, c2):
    return c1 + c2

# Subtraction
def subtract_complex_numbers(c1, c2):   
    return c1 - c2

# Multiplication
def multiply_complex_numbers(c1, c2):
    return c1 * c2

# Division
def divide_complex_numbers(c1, c2):
    if c2 == 0:
        raise ValueError("Cannot divide by zero.")
    return c1 / c2


print(add_complex_numbers(complex_num1, complex_num2))
print(subtract_complex_numbers(complex_num1, complex_num2))
print(multiply_complex_numbers(complex_num1, complex_num2))
print(divide_complex_numbers(complex_num1, complex_num2))  