import re
import os
from time import sleep

def parse_map() -> tuple[list, list]:
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    map_rows = [list(line) for line in lines[:-2]]
    regex = re.findall(r'\d+|\D', lines[-1])
    path = list(map(lambda x: int(x) if x.isdigit() else x, regex))
    start = None
    for i, row in enumerate(map_rows):
        if '.' in row:
            j = row.index('.')
            map_rows[i][j] = '>'
            start = (j,i)
            break
    
    return map_rows, path, start
                

def print_map(monkey_map: list[list[str]]):
    sleep(0.2)
    os.system("cls")
    print("\033[H") # move cursor to the top-left
    for line in monkey_map:
        print("".join(line))
    print()


def in_range(x:int, y: int, lst: list) -> bool:
    return y in range(len(lst)) and x in range(len(lst[y]))


def simulate(monkey_map: list[list[str]], path: list[int | str], start: tuple[int,int]) -> int:
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    dirs_chr = ['>', 'v', '<', '^']
    curr_pos = start
    curr_dir = (1,0)
    curr_dir_idx = 0

    for inst in path:
        if type(inst) is int: # move to dir that is facing
            for _ in range(inst):
                x, y = curr_pos
                dx, dy = curr_dir
                nx, ny = (x + dx, y + dy)

                if in_range(nx, ny, monkey_map):
                    if monkey_map[ny][nx] == '#':
                        break


                if curr_dir == (1,0) and (nx == len(monkey_map[ny]) or monkey_map[ny][nx] == ' '): # right edge
                    while in_range(nx-1, ny, monkey_map) and monkey_map[ny][nx-1] != ' ':
                        nx -= 1

                elif curr_dir == (-1,0) and (nx == -1 or monkey_map[ny][nx] == ' '): # left edge
                    while in_range(nx+1, ny, monkey_map) and monkey_map[ny][nx+1] != ' ':
                        nx += 1 

                elif curr_dir == (0,1) and (ny == len(monkey_map) or monkey_map[ny][nx] == ' '):# bottom edge
                    while in_range(nx, ny-1, monkey_map) and monkey_map[ny-1][nx] != ' ':
                        ny -= 1
                    
                elif curr_dir == (0,-1) and (ny == -1 or monkey_map[ny][nx] == ' '): # top edge
                    while in_range(nx, ny+1, monkey_map) and monkey_map[ny+1][nx] != ' ':
                        ny += 1
      
                        
                if monkey_map[ny][nx] == '.' or monkey_map[ny][nx] in dirs_chr:                                    
                    monkey_map[ny][nx] = dirs_chr[curr_dir_idx]
                    curr_pos = (nx, ny)

                print_map(monkey_map)

        else: # rotate
            curr_dir_idx = dirs.index(curr_dir)
            dir_sign = 1 if inst == "R" else -1
            next_dir_idx = (curr_dir_idx + dir_sign) % len(dirs)
            curr_dir = dirs[next_dir_idx]
            curr_dir_idx = next_dir_idx
            monkey_map[curr_pos[1]][curr_pos[0]] = dirs_chr[next_dir_idx]

        print_map(monkey_map)

    
    return curr_pos, curr_dir_idx


monkey_map, path, start = parse_map()
pos, dir = simulate(monkey_map, path, start)

col, row = pos
password = 1000 * (row+1) + 4 * (col+1) + dir

print(password)


### attempts 
# 9252 too low