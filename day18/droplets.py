

def parse_cubes() -> list[str]:
    f = open("puzzle_input.txt", "r")
    return [tuple(map(int,line.split(","))) for line in f.read().splitlines()]


def are_adjacent(pos1, pos2):
    return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])) == 1




def get_blank_spaces(cubes):
 
    blank_spaces = set()
    
    for x, y, z in cubes:
        if (x-1, y, z) in cubes:
            continue
        if (x+1, y, z) in cubes:
            continue
        if (x, y-1, z) in cubes:
            continue
        if (x, y+1, z) in cubes:
            continue
        if (x, y, z-1) in cubes:
            continue
        if (x, y, z+1) in cubes:
            continue

        blank_spaces.add((x, y, z))
        
    return blank_spaces






def exterior_surface_area(cubes, blank_spaces):

  total_exterior_surface_area = 0
  
  
  for x, y, z in cubes:

    exposed_sides = 6
    
    if (x-1, y, z) in cubes:
      exposed_sides -= 1
    if (x+1, y, z) in cubes:
      exposed_sides -= 1
    if (x, y-1, z) in cubes:
      exposed_sides -= 1
    if (x, y+1, z) in cubes:
      exposed_sides -= 1
    if (x, y, z-1) in cubes:
      exposed_sides -= 1
    if (x, y, z+1) in cubes:
      exposed_sides -= 1
      

    total_exterior_surface_area += exposed_sides
    

  for x, y, z in blank_spaces:
    exposed_sides = 0
    
    if (x-1, y, z) in cubes:
      exposed_sides += 1
    if (x+1, y, z) in cubes:
      exposed_sides += 1
    if (x, y-1, z) in cubes:
      exposed_sides += 1
    if (x, y+1, z) in cubes:
      exposed_sides += 1
    if (x, y, z-1) in cubes:
      exposed_sides += 1
    if (x, y, z+1) in cubes:
      exposed_sides += 1
      
    total_exterior_surface_area -= exposed_sides
    
  return total_exterior_surface_area