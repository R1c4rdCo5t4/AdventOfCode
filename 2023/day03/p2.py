from dataclasses import dataclass
from functools import reduce

with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

@dataclass
class Number:
    coords: list[tuple[int, int]]
    val: int

    def __hash__(self):
        return hash(tuple(self.coords))

# get numbers and coordinates first
nums: list[Number] = []
for row in range(0, len(lines)):
    coords = []
    num = ''
    for col in range(0, len(lines[row])):
        char = lines[row][col]
        if char.isdigit():
            num += char
            coords.append((row, col))
        else:
            if len(num) > 0:
                nums.append(Number(coords, int(num)))
                num = ''
                coords = []

    if len(num) > 0:
        nums.append(Number(coords, int(num)))
               
# search for gears
result = 0
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        char = lines[row][col]

        def get(r: int, c: int):
            if r in range(0, len(lines)) and c in range(0, len(lines[r])):
                return lines[r][c]
            
            return None

        def get_nearby_numbers() -> list[Number]:
            up = (row-1, col)
            up_right  = (row-1, col+1)
            right = (row, col+1)
            down_right = (row+1, col+1)
            down = (row+1, col)
            down_left = (row+1, col-1)
            left = (row, col-1)
            up_left = (row-1, col-1)

            def check_dir(r, c) -> list[Number] | None:
                char = get(r, c)
                return next((num for num in nums if char != None and char.isdigit() and (r,c) in num.coords), None)

            directions = [up, up_right, right, down_right, down, down_left, left, up_left]
            return list(set(check_dir(r, c) for r, c in directions))

        if char == '*':
            nearby = list(filter(lambda x: x != None, get_nearby_numbers()))
            if len(nearby) == 2:
                result += nearby[0].val * nearby[1].val
        
print(result) # 78272573
