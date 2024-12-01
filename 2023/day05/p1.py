import re

with open("puzzle_input.txt", "r") as f:
    blocks = f.read().split("\n\n")


seeds = re.findall("\d+", blocks[0])
print("Seeds")
print(seeds)
for block in blocks:
    print("Map")
    for line in block.split("\n")[1:]:
        mappings = line.split(" ")
        print(mappings)