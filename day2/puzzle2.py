import re

class PasswordValidator:
    def __init__(self, line: str):
        match = re.search('^(\d+)-(\d+) ([a-z]): ([a-z]+)$', line.strip())
        self.pos_a = int(match.groups()[0]) - 1
        self.pos_b = int(match.groups()[1]) - 1
        self.character, self.password = match.groups()[2:]
    
    def is_valid(self):
        return (self.password[self.pos_a] == self.character) ^ (self.password[self.pos_b] == self.character)

with open('input.txt', 'r') as f:
    validators = [PasswordValidator(line) for line in f.readlines()]
    
print(sum(validator.is_valid() for validator in validators))