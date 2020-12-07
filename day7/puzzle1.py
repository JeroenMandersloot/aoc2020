import regex

pattern = r'(.+)s contain (?:(?:\d+ ([^,.]*?)s?(?:, )?)+.$)?'


hierarchy = dict()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        match = regex.search(pattern, line)
        parent = match.captures(1)[0]
        children = set(match.captures(2))
        hierarchy[parent] = children
    

def can_contain(parent, child, hierarchy, exclude=None):
    if not exclude:
        exclude = set()
    children = hierarchy[parent] - exclude
    if child in children:
        return True
    for new_parent in children:
        if can_contain(new_parent, child, hierarchy, exclude | children):
            return True
    return False
    

print(sum(can_contain(bag, 'shiny gold bag', hierarchy) for bag in hierarchy))
