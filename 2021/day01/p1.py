with open("puzzle_input.txt") as f:
    lines = list(map(int, f.read().splitlines()))

count = 0
prev = lines[0]
for value in lines:
    if value > prev:
        count += 1
    prev = value

print(count) # 1226
