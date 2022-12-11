from dirs import *


f = open("puzzle_input.txt", "r")
dirs = parse_directories(f)
f.close()

max_dir_sum = 100000
result = 0
for dir in dirs.keys():
    dir_sum = compute_dir_size(dir, dirs)
    if dir_sum <= max_dir_sum:
        result += dir_sum


print(result) # 1297683
