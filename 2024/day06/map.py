from dataclasses import dataclass
from copy import deepcopy

obstacles = {'#', 'O'}
empty_chars = {'.', 'X'}

@dataclass
class Data:
    width: int
    height: int
    lines: list[str]
    chars: list[str]
    chars_dirs: dict[str, tuple[int, int]]

    def __iter__(self):
        return iter((self.width, self.height, self.lines, self.chars, self.chars_dirs))
    
    def copy(self):
        return Data(self.width, self.height, deepcopy(self.lines), self.chars, self.chars_dirs)

def get_puzzle_data() -> Data:
    with open("puzzle_input.txt") as f:
        lines = f.read().splitlines()

    width, height = len(lines[0]), len(lines)
    chars : list[str] = ['^', '>', 'v', '<'] # for 90 degree turns
    chars_dirs: dict[str, tuple[int, int]] = {
        '^': (0, -1), 
        'v': (0, 1), 
        '>': (1, 0), 
        '<': (-1, 0)
    }
    return Data(width, height, lines, chars, chars_dirs)

def in_bounds(x: int, y: int, width: int, height: int) -> bool:
    return x in range(0, width) and y in range(0, height)
        
def find_coords(lines, chars_dirs) -> tuple[int, int]:
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in chars_dirs.keys():
                return x, y

def walk(data: Data, on_step=None):
    width, height, lines, chars, chars_dirs = data
    x, y = find_coords(lines, chars_dirs)
    char = lines[y][x]
    visited_positions = set()

    while True:
        dx, dy = chars_dirs[char]
        nx, ny = x + dx, y + dy
        visited_positions.add((x, y))

        if not in_bounds(nx, ny, width, height):
            break

        next_char = lines[ny][nx]
        if next_char in obstacles:
            # turn 90 degrees to the right
            idx = chars.index(char)
            char = chars[(idx + 1) % len(chars)]
            # update the current cell
            lines[y] = lines[y][:x] + char + lines[y][x + 1:]

        else:
            if on_step:
                if on_step((x,y), char):
                    break # found loop, stop walking

            # update the current cell
            lines[y] = lines[y][:x] + 'X' + lines[y][x + 1:]

            # move to next cell
            lines[y + dy] = lines[y + dy][:x + dx] + char + lines[y + dy][x + dx + 1:]
            x += dx
            y += dy
    
    return visited_positions