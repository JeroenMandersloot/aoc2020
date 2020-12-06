groups = []

with open('input.txt', 'r') as f:
    group = set()
    for line in f.readlines():
        line = line.strip()
        if not line:
            groups.append(group)
            group = set()
        else:
            group |= set(line)
    if group:
        groups.append(group)

print(sum(map(len, groups)))
            