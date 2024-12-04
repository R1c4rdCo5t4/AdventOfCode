with open("puzzle_input.txt") as f:
    lines = f.read().splitlines()

target_word = "XMAS"
horizontal_asc = lines
horizontal_desc = [line[::-1] for line in lines]
vertical_asc = ["".join([line[i] for line in lines]) for i in range(len(lines[0]))]
vertical_desc = [line[::-1] for line in vertical_asc]

# top-left to bottom-right
diagonal_right_asc = \
    ["".join(lines[i][i + k] for i in range(len(lines) - k)) for k in range(len(lines))] + \
    ["".join(lines[i + k][i] for i in range(len(lines) - k)) for k in range(1, len(lines))] 

# top-right to bottom-left
diagonal_left_asc = \
    ["".join(lines[i][len(lines) - 1 - i - k] for i in range(len(lines) - k)) for k in range(len(lines))] + \
    ["".join(lines[i + k][len(lines) - 1 - i] for i in range(len(lines) - k)) for k in range(1, len(lines))]

diagonal_right_asc = [line for line in diagonal_right_asc if len(line) >= len(target_word)]
diagonal_left_asc = [line for line in diagonal_left_asc if len(line) >= len(target_word)]
diagonal_right_desc = [line[::-1] for line in diagonal_right_asc]
diagonal_left_desc = [line[::-1] for line in diagonal_left_asc]

all_lines = horizontal_asc + horizontal_desc + vertical_asc + vertical_desc + diagonal_right_asc + diagonal_right_desc + diagonal_left_asc + diagonal_left_desc
result = sum(line.count(target_word) for line in all_lines)

print(result) # 2464

