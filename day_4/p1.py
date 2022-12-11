
def fully_contains(pair: list[str]) -> bool:
    ranges = [range(int(start), int(end) + 1) for start, end in (r.split("-") for r in pair)]
    is_sub_range = lambda r1, r2: r1[0] in r2 and r1[-1] in r2
    return is_sub_range(ranges[0], ranges[1]) or is_sub_range(ranges[1], ranges[0])


f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")
pairs = [line.split(",") for line in puzzle_input]
result = sum(1 for pair in pairs if fully_contains(pair))

print(result) # 538



