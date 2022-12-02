
f = open("puzzle_input.txt", "r")
puzzle_input = f.read()

max_sums = [0, 0, 0]
for idx, elf in enumerate(puzzle_input.split("\n\n"), 1):
    curr_sum = sum([int(i) for i in elf.split("\n")])

    min_sum = min(max_sums)
    if curr_sum > min_sum:
        max_sums[max_sums.index(min_sum)] = curr_sum

print(max_sums) # 72240, 69625, 69092
print(sum(max_sums)) # 210957

