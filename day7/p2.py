from dirs import *


f = open("puzzle_input.txt", "r")
dirs = parse_directories(f)
f.close()

disk_space = 70000000
needed_space = 30000000
used_disk = compute_dir_size("/", dirs)
free_disk = disk_space - used_disk

smallest = used_disk
for dir in dirs.keys():
    dir_sum = compute_dir_size(dir, dirs)

    if free_disk + dir_sum >= needed_space and dir_sum < smallest:
        smallest = dir_sum
       

print(smallest) # 5756764

