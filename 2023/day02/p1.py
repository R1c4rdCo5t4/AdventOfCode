
with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

result = 0
cubes_dict = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for line in lines:
    parts = line.split(" ")
    game_id = int(parts[:2][1][:-1])
    sets = " ".join(parts[2:]).split(";")

    def is_possible():
        for set in sets:
            for subset in set.strip().split(", "):
                amount, color = subset.split(" ")
                if int(amount) > cubes_dict[color]:
                    return False
        return True
    
    if is_possible():
        result += game_id

print(result) # 2771

