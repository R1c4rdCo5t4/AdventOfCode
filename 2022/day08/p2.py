
def get_visible_trees(tree:int, direction: list[int] | tuple[int]) -> int:
    count = 0
    for t in direction:
        count += 1
        if t >= tree:
            break

    return count


f = open("puzzle_input.txt", "r")
puzzle_input = f.read().splitlines()
f.close()

highest_score = 0
forest = [[int(tree) for tree in line] for line in puzzle_input]

for row_idx, row in enumerate(forest):
    for col_idx, tree in enumerate(row):
        
        u = [line for line in [puzzle_input[i][col_idx] for i in range(row_idx - 1, -1, -1)]]
        l = [col for col in row[:col_idx] if col_idx > 0][::-1]
        d = [line for line in [puzzle_input[i][col_idx] for i in range(row_idx + 1, len(puzzle_input))]]
        r = [col for col in row[col_idx+1:] if col_idx < len(row) - 1]

        dirs = [list(map(int, x)) for x in [u, l, d, r]]
        col = list(zip(*forest))[col_idx]
        t = int(tree)

        left_count= get_visible_trees(t, row[:col_idx][::-1])
        right_count = get_visible_trees(t, row[col_idx+1:])
        up_count = get_visible_trees(t, col[:row_idx][::-1])
        down_count = get_visible_trees(t, col[row_idx+1:])

        score = left_count * right_count * up_count * down_count
        if score > highest_score:
            highest_score = score


print(highest_score) # 480000