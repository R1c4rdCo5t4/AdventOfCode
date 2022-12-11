from stacks import parse_stacks, rearrange_stacks, get_stack_tops

def move_crates(stcks: list[chr], amount:int, src:int, to:int) -> None:
    stcks[to].extend(stcks[src][-1:-amount-1:-1]) # add sublist to list in reverse order (lifo)
    stcks[src] = stcks[src][:-amount] # remove sublist from src


f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")
stacks = parse_stacks(puzzle_input)
rearrange_stacks(stacks, puzzle_input, move_crates)

print(get_stack_tops(stacks)) # LBLVVTVLP