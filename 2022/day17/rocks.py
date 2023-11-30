from time import sleep
from copy import deepcopy
import os


def parse_directions():
    return open("puzzle_input.txt").read()


def get_tower_height(grid):
    grid_height = len(grid)
    for height, row in enumerate(grid):
        if '#' in row:
            return grid_height - height

    return 0


def insert_rock(rock, grid, width):

    while grid and '#' not in grid[0]: # removes top empty rows
        grid.pop(0)
    
    
    for i, line in enumerate(rock): # adds rock 
        grid.insert(i, ['.'] * 2 + list(line) + ["."] * (width - len(line) - 2))


    rock_height = len(rock) 
    empty_row = ['.'] * width

    for _ in range(3): # adds 3 empty rows
        grid.insert(rock_height, empty_row[:])

    return grid



def stop_rock(grid:list[str]):
    
    for i in range(len(grid)):
        grid[i] = list("".join(grid[i]).replace("@", "#"))
            

def shift_rock(grid:list[str], dx:int, dy:int):

    positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '@']
    step = 1 if dx < 0 else -1 # which order to move @ (left/right)
    
    for i, j in positions:
        if j+dx not in range(len(grid[0])): # hit sides
            return grid # unmodified grid

        if i+dy not in range(len(grid)) or grid[i+dy][j+dx] == '#': # hit bottom
            if dy > 0:
                stop_rock(grid)

            return grid # unmodified grid
  
    for i,j in positions[::step]:
        grid[i+dy][j+dx] = '@'
        grid[i][j] = '.'
    
    return grid

 

def simulate(rock_types, dirs, max_rocks, width):

    grid = []
    rock_count = 0
    dir_idx = 0
    rock_idx = 0

    while rock_count < max_rocks:
        rock = rock_types[rock_idx]
        rock_idx = (rock_idx+1) % len(rock_types)
        rock_count += 1
        # print_grid(grid)
        insert_rock(rock, grid, width)
       
        while True: # while rock hasnt stopped moving
            
            dir = 1 if dirs[dir_idx] == '>' else -1 
            dir_idx = (dir_idx+1) % len(dirs)

            grid = shift_rock(grid, dir, 0) # left/right
            print_grid(grid)

            grid = shift_rock(grid, 0, 1) # down
            print_grid(grid)

            for row in grid:
                if '@' in row:
                    break
            else:
                break

            

    return get_tower_height(grid)
        




def print_grid(grid):
    sleep(0.5)
    os.system("cls")
    print("\033[H") # move cursor to the top-left

    for line in grid:
        print("".join(line))