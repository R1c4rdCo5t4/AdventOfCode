import functools
import string

f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")

priority_sum = 0
team_size = 3
values_dict = { item:value for value,item in enumerate(string.ascii_letters, 1) }

for idx in range(0, len(puzzle_input), team_size):
    
    elf_team = [puzzle_input[idx+i] for i in range(team_size)]
    team_badge = functools.reduce(lambda x,y: set(x) & set(y), elf_team).pop()
    priority_sum += values_dict[team_badge]

print(priority_sum) # 2488
