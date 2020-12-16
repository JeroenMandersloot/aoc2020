import re

valid = set()
tickets = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        match = re.match(r'^.+: (\d+)-(\d+) or (\d+)-(\d+)$', line)
        if match:
            a, b, c, d = map(int, match.groups())
            valid = valid | set(range(a, b+1)) | set(range(c, d+1))
        
        match = re.match(r'^(?:(\d+),?)+$', line)
        if match:
            tickets.append(list(map(int, line.split(','))))
            

print(sum(t for ticket in tickets for t in ticket if t not in valid))