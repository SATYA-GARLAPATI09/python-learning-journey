# Demonstrate the following operators in Python with suitable examples.
# i) Arithmetic Operators ii) Relational Operators iii) Assignment Operators
# iv) Logical Operators v) Bitwise Operators vi) Ternary Operator
# vii) Membership Operators viii) Identity Operators


def arithmetic_operators(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Modulus: {a} % {b} = {a % b}")


def relational_operators(a, b):
    print(f"{a} > {b} -> {a > b}")
    print(f"{a} < {b} -> {a < b}")
    print(f"{a} == {b} -> {a == b}")
    print(f"{a} != {b} -> {a != b}")
    print(f"{a} >= {b} -> {a >= b}")
    print(f"{a} <= {b} -> {a <= b}")


def assignment_operators(a, b):
    x = a
    x += b
    print(f"x = {a}; x += {b} => {x}")

    x = a
    x -= b
    print(f"x = {a}; x -= {b} => {x}")

    x = a
    x *= b
    print(f"x = {a}; x *= {b} => {x}")


def logical_operators(a, b):
    print(f"{a} and {b} => {a and b}")
    print(f"{a} or {b} => {a or b}")
    print(f"not {a} => {not a}")


def bitwise_operators(a, b):
    print(f"{a} & {b} = {a & b}")
    print(f"{a} | {b} = {a | b}")
    print(f"{a} ^ {b} = {a ^ b}")
    print(f"~{a} = {~a}")
    print(f"{a} << 1 = {a << 1}")
    print(f"{a} >> 1 = {a >> 1}")


def ternary_operator(a, b):
    larger = a if a > b else b
    print(f"Greater value between {a} and {b} is {larger}")


def membership_operators(a, b):
    numbers = [10, 20, 30, 40, 50]
    print(f"{a} in numbers -> {a in numbers}")
    print(f"{b} not in numbers -> {b not in numbers}")


def identity_operators(a, b):
    x = a
    y = b
    print(f"x = a; a is x -> {a is x}")
    print(f"b is y -> {b is y}")


def switch(choice):
    options = {
        "i": arithmetic_operators,
        "ii": relational_operators,
        "iii": assignment_operators,
        "iv": logical_operators,
        "v": bitwise_operators,
        "vi": ternary_operator,
        "vii": membership_operators,
        "viii": identity_operators,
    }

    func = options.get(choice)
    if func is None:
        raise ValueError("Invalid operator choice.")
    return func


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
except ValueError:
    print("Please enter valid integers only.")
    raise SystemExit

operator = input(
    "Choose the operator: \n"
    "i) Arithmetic Operators\n"
    "ii) Relational Operators\n"
    "iii) Assignment Operators\n"
    "iv) Logical Operators\n"
    "v) Bitwise Operators\n"
    "vi) Ternary Operator\n"
    "vii) Membership Operators\n"
    "viii) Identity Operators\n"
).strip()

try:
    selected_function = switch(operator)
    selected_function(first_number, second_number)
except ValueError as error:
    print(error)