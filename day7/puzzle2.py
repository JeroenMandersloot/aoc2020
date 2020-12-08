import regex

pattern = r'^(.+)s contain (?:(?:(\d+) ([^,.]+?)s?(?:, )?)+.$)?'


hierarchy = dict()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        match = regex.search(pattern, line.strip())
        parent = match[1]
        children = dict(zip(match.captures(3), map(int, match.captures(2))))
        hierarchy[parent] = children


def get_num_children(parent) -> int:
    children = hierarchy[parent]
    if not children:
        return 0
    return sum(children.values()) + sum(num * get_num_children(child) for child, num in children.items())
    

print(get_num_children('shiny gold bag'))
