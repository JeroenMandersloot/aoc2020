import re

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


class Passport:
    def __init__(
        self,
        byr=0,
        iyr=0,
        eyr=0,
        hgt=None,
        hcl=None,
        ecl=None,
        pid=None,
        cid=None
    ):
        self.byr = byr  # (Birth Year)
        self.iyr = iyr  # (Issue Year)
        self.eyr = eyr  # (Expiration Year)
        self.hgt = hgt  # (Height)
        self.hcl = hcl  # (Hair Color)
        self.ecl = ecl  # (Eye Color)
        self.pid = pid  # (Passport ID)
        self.cid = cid  # (Country ID)
       
    def is_valid(self):
        return 1920 <= int(self.byr) <= 2002 \
                and 2010 <= int(self.iyr) <= 2020 \
                and 2020 <= int(self.eyr) <= 2030 \
                and bool(self._is_valid_height()) \
                and bool(self.hcl) \
                and bool(re.match(r'^\#[a-f0-9]{6}$', self.hcl)) \
                and self.ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} \
                and self.pid is not None \
                and bool(re.match(r'^\d{9}$', self.pid))
    
    def _is_valid_height(self):
        if not self.hgt:
            return False
    
        match = re.search(r'(\d+)(cm|in)', self.hgt)
        if not match:
            return False
        
        height, unit = match.groups()
        height = int(height)
        
        if unit == 'cm':
            return 150 <= height <= 193
        
        if unit == 'in':
            return 59 <= height <= 76
        
        return False
          
    def __bool__(self):
        return bool(self.byr or self.iyr or self.eyr or self.hgt or self.hcl or self.ecl or self.pid or self.cid)

passports = []
with open('input.txt', 'r') as f:
    passport = Passport()
    for line in f.readlines():
        line = line.strip()
        if not line:
            passports.append(passport)
            passport = Passport()
        else:
            fields = line.split(' ')
            for field in fields:
                match = re.search(r'^(\S+):(.+)$', field)
                if match: 
                    f, v = match.groups()
                    if hasattr(passport, f):
                        setattr(passport, f, v)
    if passport:
        passports.append(passport)

for passport in passports:
    if not isinstance(passport.is_valid(), bool):
        print(passport.is_valid())
        print(passport.pid)

print(sum(map(int, (passport.is_valid() for passport in passports))))