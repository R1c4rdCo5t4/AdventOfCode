from dataclasses import dataclass, field
from string import ascii_lowercase
from collections import deque

position = tuple[int,int]

def parse_input() -> list[str]:
    f = open("puzzle_input.txt", "r")
    return f.read().splitlines()


def get_directions(row: int, col: int) -> list[position]:
    return [
        (col - 1, row), # left
        (col + 1, row), # right
        (col, row - 1), # up
        (col, row + 1)  # down
    ]
    

def get_vertex(lines: list[str], pos: position):
    if pos[1] in range(len(lines)) and pos[0] in range(len(lines[pos[1]])):
        return Vertex(pos, lines[pos[1]][pos[0]])
    else:
        return None



@dataclass
class Vertex:
    pos : position
    char : str = ""
    visited : bool = False
    steps : int = 0

    def __hash__(self) -> int:
        return hash(self.char) + id(self)

    @property
    def altitude(self):
        char = self.char
        if self.char == 'S':
            char = 'a'
        elif self.char == 'E':
            char = 'z'
            
        return ascii_lowercase.index(char)

    

def get_start_and_end(lines: list[str]) -> tuple[Vertex, Vertex] | None:
    start = None
    end = None

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            
            if char == 'S':
                start = Vertex((col, row), char)

            elif char == 'E':
                end = Vertex((col, row), char)

            if start and end:
                return start, end
    return None

@dataclass
class Graph:
    graph : dict[position, set[Vertex]] = field(default_factory=dict)


    @staticmethod
    def build(lines: list[str]):
        g = Graph()
        for row, line in enumerate(lines):
            for col, chr in enumerate(line):
                pos = (col, row)
                curr = Vertex(pos, chr)
                adjacent = [v for dir in get_directions(row, col) if (v := get_vertex(lines, dir))]
                nodes = set()
                for vertex in adjacent:
                    if vertex.altitude - curr.altitude <= 1:
                        nodes.add(vertex)

                g.graph[pos] = nodes

        return g


    
    def BFS(self, start:Vertex, end:Vertex) -> int:
        
        for set in self.graph.values():
            for v in set:
                v.visited = False

        steps = 0
        queue = []
        queue.append(start)
        while queue:
            curr = queue.pop(0)
            steps = curr.steps
            if curr.pos == end.pos:
                return steps

            for v in self.graph[curr.pos]:
                if not v.visited:
                    v.steps = steps + 1
                    v.visited = True
                    queue.append(v)

        return -1
