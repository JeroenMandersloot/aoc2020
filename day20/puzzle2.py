import re
import numpy as np
from typing import List, Tuple, Optional
from enum import Enum
from itertools import product
from tqdm import tqdm
from functools import reduce
import pickle 
import os

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
    
    def match_free(self, other: 'Tile') -> List[Tuple[int, Flip, int]]:
        rotations = [0, 90, 180, 270]
        flips = [None, Flip.LR, Flip.TB]
        return [(rotation, flip, side) for rotation, flip in product(rotations, flips) for side in self.rotate(rotation).flip(flip).match(other)]
    
    def match_free_all(self, other: 'Tile') -> List[Tuple[int, Flip, int, Flip, int]]:
        rotations = [0, 90, 180, 270]
        flips = [None, Flip.LR, Flip.TB]
        return [(rotation_a, flip_a, rotation_b, flip_b, side) 
                for rotation_a, flip_a in product(rotations, flips) 
                for rotation_b, flip_b in product(rotations, flips) 
                for side in self.rotate(rotation_a).flip(flip_a).match(other.rotate(rotation_b).flip(flip_b))]
    
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
    
    def compute_roughness(self):
        sea_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
        pattern = np.array([[int(c == "#") for c in line] for line in sea_monster.strip("\n").split("\n")])
        layout = np.copy(self.layout)
        height, width = self.layout.shape
        num_sea_monsters = 0
        for y in range(height):
            for x in range(width):
                extract = layout[y:y+pattern.shape[0], x:x+pattern.shape[1]]
                if extract.shape != pattern.shape:
                    break
                if all(extract[pattern == 1] == 1):
                    num_sea_monsters += 1
                    extract[pattern == 1] = -1
        if not num_sea_monsters:
            raise LookupError("No sea monsters found!")
        return np.sum(layout == 1)
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.tile_id == other.tile_id and np.array_equal(self.layout, other.layout)
    
    def __str__(self) -> str:
        return "\n".join("".join('#' if cell == 1 else '.' if cell == 0 else 'O' for cell in row) for row in self.layout)
    
    def __hash__(self) -> int:
        return hash(self.id)


class Puzzle:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.grid = [[None] * self.width for _ in range(self.height)]
    
    def place(self, y, x, tile: Tile):
        self.grid[y][x] = tile
        
    @staticmethod
    def get_matches(tiles: List[Tile]):
        matches = dict()
        for a in tqdm(tiles):
            matches[a] = dict()
            for b in tiles:
                if b != a:
                    m = a.match_free(b)
                    if m:
                        matches[a][b] = m        
        return matches
     
    def compute_roughness(self):
        rotations = [0, 90, 180, 270]
        flips = [None, Flip.LR, Flip.TB]
        tile = Tile(None, self.layout)
        for rotation, flip in product(rotations, flips):
            try:
                return tile.rotate(rotation).flip(flip).compute_roughness()
            except LookupError:
                pass
        raise ValueError("No sea monsters found :(")
    
    @property
    def layout(self):
        # Cut borders
        tile_height, tile_width = map(lambda t: t - 2, self.grid[0][0].layout.shape)
        
        layout_height = tile_height * self.height
        layout_width = tile_width * self.width
        
        layout = np.zeros((layout_height, layout_width))
        for y in range(self.height):
            for x in range(self.width):
                layout[y*tile_height:(y+1)*tile_height, x*tile_width:(x+1)*tile_width] = self.grid[y][x].layout[1:-1, 1:-1]
        
        return layout
        
    
    def solve(self, tiles: List[Tile]):
        matches = self.get_matches(tiles)
                        
        corners = [a for a, m in matches.items() if len(m) == 2]
        edges = [a for a, m in matches.items() if len(m) == 3]
        others = [a for a, m in matches.items() if len(m) == 4]
        
        puzzle.place(0, 0, corners[0])
    
        for y in range(1, self.height - 1):
            candidate = self.resolve(y, 0, edges)
        self.resolve(self.height - 1, 0, corners)
            
        for x in range(1, self.width - 1):
            candidate = self.resolve(0, x, edges)
        self.resolve(0, self.width - 1, corners)

        for y in range(1, self.height - 1):
            candidate = self.resolve(y, self.width - 1, edges)
            
        for x in range(1, self.width - 1):
            candidate = self.resolve(self.height - 1, x, edges)
        self.resolve(self.height - 1, self.width - 1, corners)
            
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                self.resolve(y, x, others)
    
    def resolve(self, y, x, tiles: List[Tile], remove_after: bool = True) -> Tile:
        neighbours = (
            self.grid[y-1][x] if y > 0 else None,
            self.grid[y][x+1] if x + 1 < self.width else None,
            self.grid[y+1][x] if y + 1 < self.height else None,
            self.grid[y][x-1] if x > 0 else None
        )
        
        if not any(neighbours):
            raise ValueError("Can't resolve tile without any neighbours")
            
        for tile in tiles:
            possibilities = None
            for side, neighbour in enumerate(neighbours):
                if neighbour:
                    allowed_by_neighbour = set()
                    for rotation, flip, side_ in tile.match_free(neighbour):
                        if side_ == side:
                            allowed_by_neighbour.add(tile.rotate(rotation).flip(flip))
                    if possibilities is None:
                        possibilities = allowed_by_neighbour
                    else:
                        possibilities = possibilities.intersection(allowed_by_neighbour)

            if len(possibilities) == 1:
                candidate = possibilities.pop()
                self.place(y, x, candidate)
                tiles.remove(tile)
                return candidate
            
            if len(possibilities) > 1:
                raise ValueError("More than 1 candidate tile")
         
        raise ValueError("No candidate tiles")
        
   

def parse_tile(tile: str) -> Tile:
    tile_id, *layout = tile.split("\n")
    _, tile_id = tile_id.split(' ')
    tile_id = int(tile_id[:-1])
    layout = np.array([[int(cell == '#') for cell in row] for row in layout])
    return Tile(int(tile_id), layout)
    
    
with open('input.txt', 'r') as f:
    tiles = list(map(parse_tile, f.read().split("\n\n")))


puzzle = Puzzle(12, 12)
puzzle.solve(tiles)
print(puzzle.compute_roughness())






