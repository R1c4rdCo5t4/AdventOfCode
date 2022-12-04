
def has_overlap(pair: list[str]) -> bool:
    ranges = [range(int(start), int(end) + 1) for start, end in (r.split("-") for r in pair)]
    return bool(set(ranges[0]) & set(ranges[1]))

f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")
pairs = [line.split(",") for line in puzzle_input]
result = sum(1 for pair in pairs if has_overlap(pair))

print(result) # 792
