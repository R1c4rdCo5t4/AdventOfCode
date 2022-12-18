from rocks import *

dirs = parse_directions()
grid_width = 7

rock_types = (
    ["@@@@"],
    [".@.","@@@",".@."],
    ["..@","..@","@@@"],
    ["@","@","@","@"],
    ["@@","@@"]
)

tower_height = simulate(rock_types, dirs, 2022, grid_width)

print(tower_height) # 3141
