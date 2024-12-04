with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

result = 0
center_char = "A"
other_chars = ["M", "S"]
for row in range(1, len(lines)-1):
    for col in range(1, len(lines[0])-1):
        center = lines[row][col]
        if center == center_char: # check surroundings
            top_left = lines[row-1][col-1]
            top_right = lines[row-1][col+1]
            bottom_left = lines[row+1][col-1]
            bottom_right = lines[row+1][col+1]
            if (top_left == top_right and bottom_left == bottom_right and top_left != bottom_left and
                top_left in other_chars and bottom_left in other_chars) or \
                (top_left == bottom_left and top_right == bottom_right and top_left != top_right and
                top_left in other_chars and top_right in other_chars):
                result += 1

print(result) # 1982
