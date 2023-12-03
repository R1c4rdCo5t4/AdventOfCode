
with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

def is_symbol(char: str | None) -> bool:
    return char != None and char != '.' and (not char.isdigit())

result = 0
num_str = ''
found_part = False
for row in range(0, len(lines)):
    for col in range(0, len(lines[row])):
        char = lines[row][col]

        def get(r: int, c: int) -> str | None:
            if r in range(0, len(lines)) and c in range(0, len(lines[r])):
                return lines[r][c]

            return None

        def has_nearby_part() -> bool:
            up = get(row-1, col) 
            up_right = get(row-1, col+1)
            right = get(row, col+1)
            down_right = get(row+1, col+1)
            down = get(row+1, col)
            down_left = get(row+1, col-1)
            left = get(row, col-1)
            up_left = get(row-1, col-1)
            directions = [up, up_right, right, down_right, down, down_left, left, up_left]
            return any(list(map(lambda x: is_symbol(x), directions)))

        # append digit to num_str
        if char.isdigit():
            num_str += char

            ## check nearby symbols
            if not found_part:
                if has_nearby_part():
                    found_part = True

        # stopped looking for more digits
        if not char.isdigit():

            # collect number
            if found_part and num_str.isnumeric():
                result += int(num_str)

            # reset
            num_str = ''
            found_part = False
        

print(result) # 536202
