import re
import numpy as np
from typing import List, Tuple, Optional
from enum import Enum
from itertools import product
from tqdm import tqdm
from functools import reduce

class Flip(Enum):
    LR = 1
    TB = 2


class Tile:
    def __init__(self, tile_id: int, layout: np.ndarray):
        self.tile_id = tile_id
        self.layout = layout
    
    def rotate(self, degrees: int) -> 'Tile':
        num_turns = degrees // 90
        return Tile(self.tile_id, np.rot90(self.layout, num_turns, (1, 0)))
    
    def flip(self, flip: Optional[Flip] = Flip.LR) -> 'Tile':
        layout = self.layout[:, ::-1] if flip == Flip.LR else self.layout[::-1, :] if flip == Flip.TB else self.layout
        return Tile(self.tile_id, layout)
    
    def match(self, other: 'Tile') -> List[int]:
        res = []
        for i, side in enumerate(self.sides):
            j = (i + 2) % 4
            if side == other.sides[j]:
                res.append(i)
        return res
    
    def match_potential(self, other: 'Tile') -> List[Tuple[int, Flip, int, int]]:
        rotations = [0, 90, 180, 270]
        flips = [None, Flip.LR, Flip.TB]
        return [(rotation, flip, side) for rotation, flip in product(rotations, flips) for side in self.rotate(rotation).flip(flip).match(other)]
        
    
    @property
    def sides(self):
        return list(map(tuple, [
            self.layout[0, :],
            self.layout[:, -1],
            self.layout[-1, :],
            self.layout[:, 0]
        ]))
        
    @property
    def id(self) -> int:
        return self.tile_id
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.tile_id == other.tile_id and np.array_equal(self.layout, other.layout)
    
    def __str__(self) -> str:
        return "\n".join(" ".join('#' if cell else '.' for cell in row) for row in self.layout)
    
    def __hash__(self) -> int:
        return hash(self.id)
   

def parse_tile(tile: str) -> Tile:
    tile_id, *layout = tile.split("\n")
    _, tile_id = tile_id.split(' ')
    tile_id = int(tile_id[:-1])
    layout = np.array([[int(cell == '#') for cell in row] for row in layout])
    return Tile(int(tile_id), layout)
    
    
with open('input.txt', 'r') as f:
    tiles = list(map(parse_tile, f.read().split("\n\n")))


corners = [a.id for a in tqdm(tiles) if 2 == sum(map(bool, (a.match_potential(b) for b in tiles if a != b)))]
print(reduce(lambda a, b: a * b, corners, 1))

        