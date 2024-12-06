from map import *

data = get_puzzle_data()
initial_copy = data.copy()
starting_pos = find_coords(data.lines, data.chars_dirs)
visited_positions = walk(data)
possible_positions = visited_positions - set([starting_pos])
correct_positions = set()

for position in possible_positions: # brute force all possibilities
    history = set()

    def on_step(pos, char) -> None:
        if (pos, char) in history:
            correct_positions.add(position)
            return True

        history.add((pos, char))
        return False

    # substitute position in the data with O
    data = initial_copy.copy()
    x, y = position
    data.lines[y] = data.lines[y][:x] + 'O' + data.lines[y][x + 1:]
    walk(data, on_step=on_step)

print(len(correct_positions)) # 1482