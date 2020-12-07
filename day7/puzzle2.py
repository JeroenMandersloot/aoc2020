import regex

pattern = r'(.+)s contain (?:(?:(\d+) ([^,.]*?)s?(?:, )?)+.$)?'
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    matches = [regex.search(pattern, line) for line in lines]


hierarchy = dict()
for line, match in zip(lines, matches):
    parent = match.captures(1)[0]
    hierarchy[parent] = dict(zip(match.captures(3), map(int, match.captures(2))))


def get_num_children_recursive(parent, hierarchy) -> int:
    children = hierarchy[parent]
    if not children:
        return 0
    return sum(children.values()) + sum(num * get_num_children_recursive(child, hierarchy) for child, num in children.items())
        
    
print(get_num_children_recursive('shiny gold bag', hierarchy))
