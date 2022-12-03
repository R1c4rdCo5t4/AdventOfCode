
f = open("puzzle_input.txt", "r")
puzzle_input = f.read()

priority_sum = 0
priority_value = lambda it: ord(it) - (96 if(it.islower()) else 38)

for line in puzzle_input.split("\n"):
    middle = len(line) // 2
    first = line[:middle]
    second = line[middle:]

    for item in second:
        if item in first:
            priority_sum += priority_value(item)
            break


print(priority_sum) # 7863
