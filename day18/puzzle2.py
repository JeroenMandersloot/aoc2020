import re

class Float:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        return Float(self.v * other.v)
        
    def __mul__(self, other):
        return Float(self.v + other.v)


res = 0
table = str.maketrans({'+': '*', '*': '+'})
with open('input.txt', 'r') as f:
    for line in f.readlines():
        expr = line.strip()
        expr = expr.translate(table)
        expr = re.sub(r'(\d+)', r'Float(\1)', expr)
        value = eval(expr).v
        res += value

print(res)