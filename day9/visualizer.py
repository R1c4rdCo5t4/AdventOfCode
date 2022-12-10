from dataclasses import dataclass, field


@dataclass
class Grid:
    width : int
    height: int
    grid : list[list[str]] = field(default_factory=list)

    def __post_init__(self):
        for _ in range(self.height):
            row = ['.'] * self.width
            self.grid.append(row)

    
    def print(self):
        for line in self.grid[::-1]:
            print("".join(line))

    def remove(self, pos):
        self.grid[pos[1]][pos[0]] = '.'

    def add(self, pos, char):
        self.grid[pos[1]][pos[0]] = char