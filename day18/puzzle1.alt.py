import re


def resolve_sub_expression(expr) -> str:
    if hasattr(expr, 'group'):
        expr = expr.group(1)
    operands = re.findall(r'(\d+)', expr)
    operators =  re.findall(r'([+*])', expr)
    value = operands.pop(0)
    for o, b in zip(operators, operands):
        value = eval(f"{value} {o} {b}")
    return str(value)


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