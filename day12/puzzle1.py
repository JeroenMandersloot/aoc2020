import re


x = 0
y = 0
facing = 'E'

directions = ('N', 'E', 'S', 'W')

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        action, value = re.match(r'([A-Z])(\d+)', line.strip()).groups()
        value = int(value)
        
        if action == 'F':
            action = facing
        elif action == 'L':
            value = (value / 90) % 4
            facing = directions[int((directions.index(facing) + len(directions) - value) % len(directions))]
        elif action == 'R':
            value = (value / 90) % 4
            facing = directions[int((directions.index(facing) + len(directions) + value) % len(directions))]
        
        if action == 'E':
            x += value
        if action == 'S':
            y -= value
        if action == 'N':
            y += value
        if action == 'W':
            x -= value
            
print(f"{x}, {y}. Manhattan: {abs(x)+abs(y)}")