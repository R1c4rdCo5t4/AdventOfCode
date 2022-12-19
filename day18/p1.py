
def parse_input() -> list[str]:
    f = open("puzzle_input.txt", "r")
    return f.read().splitlines()

def are_adjacent(pos1, pos2):
    return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])) == 1


lines = parse_input()
surface_area = 0

for idx, line in enumerate(lines):
    x1, y1, z1 = map(int, line.split(","))
    curr_area = 6
    
    for next_line in lines[idx:]:
        x2, y2, z2 = map(int, next_line.split(","))
        if are_adjacent((x1,y1,z1), (x2,y2,z2)):
            curr_area -= 2
        
    surface_area += curr_area

print(surface_area) # 4500
