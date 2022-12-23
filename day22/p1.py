import re

def parse_map() -> tuple[list, list]:
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    map_rows = [list(line) for line in lines[:-2]]
    regex = re.findall(r'\d+|\D', lines[-1])
    path = list(map(lambda x: int(x) if x.isdigit() else x, regex))
    
    for i, row in enumerate(map_rows):
        if '.' in row:
            map_rows[i][row.index('.')] = '>'
            break
    
    return map_rows, path
                

def print_map(monkey_map: list[list[str]]):
    for line in monkey_map:
        print("".join(line))


def simulate(monkey_map: list[list[str]], path: list[int | str]) -> None:

    for inst in path:
        if type(inst) is int: # move to dir that is facing
            pass 
        else: # rotate
            pass



monkey_map, path = parse_map()
print(path)

print_map(monkey_map)