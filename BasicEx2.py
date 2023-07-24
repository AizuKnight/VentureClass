# Building a better calculator

def calculate(first: int, op: str, second: int):
    if op == "+":
        return first+second
    elif op == "-":
        return first-second
    elif op == "*":
        return first*second
    elif op == "/":
        return first/second


first_term = int(input("First term: "))
operator = input("Operator: ")
second_term = int(input("Second term: "))
print(calculate(first_term, operator, second_term))
