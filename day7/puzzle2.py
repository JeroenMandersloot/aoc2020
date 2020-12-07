import regex

pattern = r'(.+)s contain (?:(?:(\d+) ([^,.]*?)s?(?:, )?)+.$)?'


hierarchy = dict()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        match = regex.search(pattern, line.strip())
        parent = match.captures(1)[0]
        hierarchy[parent] = dict(zip(match.captures(3), map(int, match.captures(2))))


def get_num_children_recursive(parent) -> int:
    children = hierarchy[parent]
    if not children:
        return 0
    return sum(children.values()) + sum(num * get_num_children_recursive(child) for child, num in children.items())
        
    
print(get_num_children_recursive('shiny gold bag'))
