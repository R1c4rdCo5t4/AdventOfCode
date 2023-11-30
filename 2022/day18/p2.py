from droplets import *


cubes = parse_cubes()

max_x = max(x for x, _, _ in cubes)
max_y = max(y for _, y, _ in cubes)
max_z = max(z for _, _, z in cubes)

spaces = get_blank_spaces(cubes, max_x, max_y, max_z)
# print(spaces)

print(exterior_surface_area(cubes, spaces))


