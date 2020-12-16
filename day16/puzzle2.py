import re

valid = set()
validator = dict()
tickets = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        match = re.match(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
        if match:
            field = match.groups()[0]
            a, b, c, d = map(int, match.groups()[1:])
            values = set(range(a, b+1)) | set(range(c, d+1))
            validator[field] = values
            valid = valid | values
        
        match = re.match(r'^(?:(\d+),?)+$', line)
        if match:
            ticket = list(map(int, line.split(',')))
            for t in ticket:
                if all(t in valid for t in ticket):
                    tickets.append(ticket)



my_ticket, *tickets = tickets
field_candidates = []
values_grouped_by_position = list(map(set, zip(*tickets)))


for vap in values_grouped_by_position:
    candidates = []
    for f, vs in validator.items():
        if vap.intersection(vs) == vap:
            candidates.append(f)
    field_candidates.append(candidates)
    

known_fields = [None] * len(field_candidates)
while not all(known_fields):
    for i, fc in enumerate(field_candidates):
        if len(fc) == 1:
            lock = fc[0]
            known_fields[i] = lock
            for fc_ in field_candidates:
                if lock in fc_:
                    fc_.remove(lock)
            break

res = 1
for f, v in zip(known_fields, my_ticket):
    if f.startswith('departure'):
        res *= v

print(res)

