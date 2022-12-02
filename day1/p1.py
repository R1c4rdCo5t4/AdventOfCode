
f = open("puzzle_input.txt", "r")
puzzle_input = f.read()

max_idx = 0
max_sum = 0
for idx, elf in enumerate(puzzle_input.split("\n\n"), 1):
    curr_sum = sum([int(i) for i in elf.split("\n")])
    if curr_sum > max_sum:
        max_sum = curr_sum
        max_idx = idx

print(max_sum) # 72240

