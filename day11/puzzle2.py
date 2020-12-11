import numpy as np


class SeatingMap:
    def __init__(self, seating_map):
        self.seating_map = seating_map
        self.height, self.width = self.seating_map.shape
    
    def get_visible_seats(self, x, y):
        xmods = list(range(1, self.width))
        ymods = list(range(1, self.height))
        visible_seats = []
        for xm, ym in [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]:
            for xmod, ymod in zip(xmods, ymods):
                xn = x + xmod * xm
                yn = y + ymod * ym
                if xn >= self.width or xn < 0 or yn >= self.height or yn < 0:
                    break
                if self.seating_map[yn, xn] != '.':
                    visible_seats.append((xn, yn))
                    break
        return visible_seats
    
    def get_num_occupied_visible_seats(self, x, y):
        visible_seats = self.get_visible_seats(x, y)
        return sum(self.seating_map[y, x] == '#' for x, y in visible_seats)
    
    def get_num_occupied_seats(self):
        return sum(self.seating_map[y, x] == '#' for x in range(self.width) for y in range(self.height))
    
    def flip_seat(self, x, y):
        current = self.seating_map[y, x]
        if current == 'L':
            self.seating_map[y, x] = '#'
        if current == '#':
            self.seating_map[y, x] = 'L'
            
    @classmethod
    def from_file(cls, path: str):
        with open(path, 'r') as f:
            seating_map = np.array([list(line.strip()) for line in f.readlines()])
            return cls(seating_map)
    
    def update(self):
        new_seating_map = self.__class__(self.seating_map.copy())
        for y in range(self.height):
            for x in range(self.width):
                seat = self.seating_map[y, x]
                d = self.get_num_occupied_visible_seats(x, y)
                if seat == 'L' and not d or seat == '#' and d >= 5:
                    new_seating_map.flip_seat(x, y)
        return new_seating_map

    def __eq__(self, other):
        return isinstance(other, self.__class__) and np.array_equal(self.seating_map, other.seating_map)
    
    def __str__(self):
        return "\n".join("".join(row) for row in self.seating_map)


seating_map = SeatingMap.from_file('input.txt')
while True:
    new_seating_map = seating_map.update()
    if seating_map == new_seating_map:
        print(seating_map.get_num_occupied_seats())
        break
    seating_map = new_seating_map
