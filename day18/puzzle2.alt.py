import re


def resolve_sub_expression(expr) -> str:

    def resolve_addition(addition):
        a, b = map(int, addition.groups())
        return str(a + b)

    def resolve_multiplication(multiplication):
        a, b = map(int, multiplication.groups())
        return str(a * b)
    
    if hasattr(expr, 'groups'):
        expr = expr.group(1)
    
    while True:
        expr, num_replacements = re.subn(r'(\d+)\s*\+\s*(\d+)', resolve_addition, expr)
        if not num_replacements:
            break
            
    while True:
        expr, num_replacements = re.subn(r'(\d+)\s*\*\s*(\d+)', resolve_multiplication, expr)
        if not num_replacements:
            break
            
    return str(expr)


def resolve_expression(expr: str) -> str:
    while True:
        expr, num_replacements = re.subn(r'\(([^()]+)\)', resolve_sub_expression, expr)
        if not num_replacements:
            break
    
    return resolve_sub_expression(expr)  


res = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        expr = line.strip()
        value = int(resolve_expression(expr))
        res += value

print(res)