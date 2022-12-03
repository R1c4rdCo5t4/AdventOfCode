import functools

f = open("puzzle_input.txt", "r")
puzzle_input = f.read()
puzzle_input_lines = puzzle_input.split("\n")

priority_sum = 0
team_size = 3
priority_value = lambda it: ord(it) - (96 if(ord(it) in range(ord('a'), ord('z')+1)) else 38)

for lineidx in  range(0, len(puzzle_input_lines), team_size):
    
    elf_team = [puzzle_input_lines[lineidx+i] for i in range(team_size)]
    team_item = functools.reduce(lambda x,y: set(x) & set(y), elf_team)
    priority_sum += priority_value(team_item.pop())

print(priority_sum) # 2488

