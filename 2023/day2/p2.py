from functools import reduce

with open("puzzle_input.txt", "r") as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    parts = line.split(" ")
    sets = " ".join(parts[2:]).split(";")
    cubes_dict = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for set in sets:
        for subset in set.strip().split(", "):
            amount, color = subset.split(" ")
            if int(amount) > cubes_dict[color]:
                cubes_dict[color] = int(amount)

    result += reduce(lambda x, y: x * y, cubes_dict.values())

print(result) # 70924
