import math


def parse_input() -> list[tuple[str, int]]:
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    return [(dir, int(val)) for (dir, val) in [tuple(line.strip().split()) for line in lines]]


def get_move_direction(dir: str) -> tuple[int, int]:
    directions = { 'U': (0,1), 'R': (1, 0), 'D': (0,-1), 'L': (-1,0) }
    return directions[dir]


def move_node(node: tuple[int,int], dir: tuple[int,int]) -> tuple[int,int]:
    return (node[0] + dir[0], node[1] + dir[1])


def update_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    
    if abs(dx) <= 1 and abs(dy) <= 1: # head and tail are already adjacent, dont move tail
        return tail
    
    new_tail_pos = (tail[0] + math.copysign(1, dx), tail[1] + math.copysign(1, dy))

    if dx == 0: # moving along the x-axis
        return (tail[0], new_tail_pos[1])
        
    if dy == 0: # moving along the y-axis
        return (new_tail_pos[0], tail[1])
    
    return new_tail_pos # moving diagonally




