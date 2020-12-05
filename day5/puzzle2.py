import math

class Pass:
    def __init__(self, encoding):
        self.row_encoding = encoding[:7]
        self.col_encoding = encoding[7:]
    
    @staticmethod
    def _to_num(a: str, b: str, s: str):
        l = 0
        r = 2 ** len(s) - 1
        for c in s:
            d = math.ceil((r - l) / 2)
            if c == a:
                r -= d
            elif c == b:
                l += d
            else:
                raise ValueError(f"Invalid encoding: {s} ({c})")
        if l == r:
            return l
        raise ValueError(f"Inconclusive! l: {l}, r: {r}")
            
    
    @property
    def row(self):
        return self._to_num('F', 'B', self.row_encoding)
    
    @property
    def col(self):
        return self._to_num('L', 'R', self.col_encoding)
    
    @property
    def id(self):
        return self.row * 8 + self.col


with open('input.txt', 'r') as f:
    passes = [Pass(line.strip()) for line in f.readlines()]


cache = dict()
for p in passes:
    cache[(p.row, p.col)] = p

for r in range(128):
    missing_seats_in_row = []
    for c in range(8):
        if (r, c) not in cache:
            missing_seats_in_row.append(c)
    if len(missing_seats_in_row) == 1:
        c = missing_seats_in_row[0]
        print(f"Row: {r}, Col: {c}")
        print(r * 8 + c)
        break




