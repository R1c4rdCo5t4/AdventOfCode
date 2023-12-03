
with open("puzzle_input.txt") as file:
    lines = file.read().splitlines()

numbers = ["".join(filter(lambda x: x.isdigit(), line)) for line in lines]
result = sum(int(num[0] + num[-1]) for num in numbers)
print(result) # 55108
