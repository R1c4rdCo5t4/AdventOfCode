with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    winning, mine =  [card.split(" ") for card in " ".join(line.split(" ")[2:]).split("|")]
    winning = [c for c in winning if c != ""]
    mine = [c for c in mine if c != ""]
    common = len(set(winning).intersection(mine))
    result +=  0 if common == 1 else int(pow(2, common - 1))

print(result) # 18634

