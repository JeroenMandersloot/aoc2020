from functools import reduce

groups = []

with open('input.txt', 'r') as f:
    group = []
    for line in [*f.readlines(), "\n"]:
        line = line.strip()
        if not line:
            if not group:
                continue
            if len(group) == 1:
                groups.append(group[0])
            else:
                groups.append(reduce(lambda a, b: a.intersection(b), group[1:], group[0]))
            group = []
        else:
            group.append(set(line))

print(sum(map(len, groups)))
            