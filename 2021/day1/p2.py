with open("puzzle_input.txt") as f:
    lines = list(map(int, f.read().splitlines()))

count = 0
window_size = 3
prev = sum(lines[:window_size])
for i in range(0, len(lines) - window_size + 1):
    value = sum(lines[i:i+window_size])
    if value > prev:
        count += 1
    prev = value

print(count) # 1252
