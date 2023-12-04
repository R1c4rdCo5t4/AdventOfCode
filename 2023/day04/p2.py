from cards import get_matches

with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

result = 0
def scratch_card(start, end) -> int:
    global result
    for i in range(start, end):
        result += 1
        line = lines[i]
        matching = get_matches(line)
        scratch_card(i+1, i+1+matching)
        
scratch_card(0, len(lines))
print(result) # 5921508
