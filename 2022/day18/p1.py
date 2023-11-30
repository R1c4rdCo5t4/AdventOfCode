from droplets import *


cubes = parse_cubes()

surface_area = 0

for idx, cube in enumerate(cubes):
    x1, y1, z1 = cube
    curr_area = 6
    
    for next_cube in cubes[idx:]:
        x2, y2, z2 = next_cube
        if are_adjacent((x1,y1,z1), (x2,y2,z2)):
            curr_area -= 2
        
    surface_area += curr_area

print(surface_area) # 4500
