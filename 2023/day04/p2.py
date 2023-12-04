
with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

def get_num_of_matching_nums(line: str) -> int:
    winning, mine =  [card.split(" ") for card in " ".join(line.split(" ")[2:]).split("|")]
    winning = [c for c in winning if c != ""]
    mine = [c for c in mine if c != ""]
    return len(set(winning).intersection(mine))

result = 0
def card(start, end) -> int:
    global result
    for i in range(start, end):
        result += 1
        line = lines[i]
        matching = get_num_of_matching_nums(line)
        card(i+1, i+1 + matching)
        
card(0, len(lines))
print(result) # 5921508
