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


print(max(p.id for p in passes))