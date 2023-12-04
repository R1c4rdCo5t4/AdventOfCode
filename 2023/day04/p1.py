from cards import get_matches

with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    matches = get_matches(line)
    result += 0 if matches == 1 else int(pow(2, matches - 1))

print(result) # 18634

