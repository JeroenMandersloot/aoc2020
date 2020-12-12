import re


x = 0
y = 0
wx = 10
wy = 1

directions = ('N', 'E', 'S', 'W')

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        action, value = re.match(r'([A-Z])(\d+)', line.strip()).groups()
        value = int(value)
        
        if action == 'F':
            x += wx * value
            y += wy * value
        elif action == 'L':
            value = (value // 90) % 4
            for _ in range(value):
                wx, wy = -wy, wx
        elif action == 'R':
            value = (value // 90) % 4
            for _ in range(value):
                wx, wy = wy, -wx
        
        if action == 'E':
            wx += value
        if action == 'S':
            wy -= value
        if action == 'N':
            wy += value
        if action == 'W':
            wx -= value
            
print(f"{x}, {y}. Manhattan: {abs(x)+abs(y)}")