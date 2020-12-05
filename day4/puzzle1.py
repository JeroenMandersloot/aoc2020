import re

class Passport:
    def __init__(
        self,
        byr=None,
        iyr=None,
        eyr=None,
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
        return bool(self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid)

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


print(sum(passport.is_valid() for passport in passports))