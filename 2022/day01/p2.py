
f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n\n")

max_sums = [0, 0, 0]
for elf in puzzle_input:
    curr_sum = sum([int(i) for i in elf.split("\n")])
    min_sum = min(max_sums)

    if curr_sum > min_sum:
        max_sums[max_sums.index(min_sum)] = curr_sum

print(sum(max_sums)) # 210957
