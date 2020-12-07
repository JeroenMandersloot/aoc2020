import regex

pattern = r'(.+)s contain (?:(?:\d+ ([^,.]*?)s?(?:, )?)+.$)?'


hierarchy = dict()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        match = regex.search(pattern, line.strip())
        parent = match.captures(1)[0]
        hierarchy[parent] = set(match.captures(2))
    

def can_contain(parent, child):
    children = hierarchy[parent]
    if child in children:
        return True
    return any(can_contain(p, child) for p in children)
    

print(sum(can_contain(bag, 'shiny gold bag') for bag in hierarchy))
