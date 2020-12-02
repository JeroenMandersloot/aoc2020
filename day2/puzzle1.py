import re

class PasswordValidator:
    def __init__(self, line: str):
        match = re.search('^(\d+)-(\d+) ([a-z]): ([a-z]+)$', line.strip())
        self.min_occurrences = int(match.groups()[0])
        self.max_occurrences = int(match.groups()[1])
        self.character, self.password = match.groups()[2:]
    
    def is_valid(self):
        return self.min_occurrences <= self.password.count(self.character) <= self.max_occurrences

with open('input.txt', 'r') as f:
    validators = [PasswordValidator(line) for line in f.readlines()]
   
print(sum(validator.is_valid() for validator in validators))