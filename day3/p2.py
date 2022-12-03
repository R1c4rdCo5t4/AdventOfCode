import functools
import string

f = open("puzzle_input.txt", "r")
puzzle_input = f.read()
puzzle_input_lines = puzzle_input.split("\n")

priority_sum = 0
team_size = 3
values_dict = { item:value for value,item in enumerate(string.ascii_letters, 1) }

for idx in range(0, len(puzzle_input_lines), team_size):
    
    elf_team = [puzzle_input_lines[idx+i] for i in range(team_size)]
    team_item = functools.reduce(lambda x,y: set(x) & set(y), elf_team)
    priority_sum += values_dict[team_item.pop()]

print(priority_sum) # 2488
