
f = open("puzzle_input.txt", "r")
puzzle_input = f.read()

elfs = puzzle_input.split("\n\n")
max_sum = 0
for elf in elfs:
    curr_sum = sum([int(i) for i in elf.split("\n")])
    if curr_sum > max_sum:
        max_sum = curr_sum


print(max_sum) # 72240

