

def get_stacks(input_lines: list[str]) -> list[chr] | None:
    stack_list = [] # list to store all stacks
    for stack_idx, line in enumerate(input_lines):
        stack_list.append([]) # create list for next stack

        for i in range(1,len(line), 4):
            crate = line[i]
            if(crate == '1'): # finished reading stacks
                stack_list.pop() # remove empty list
                stck = [list(map(str, col)) for col in zip(*stack_list)] # get stack collumns
                return [s[::-1] for s in stck] # reverse stack
            
            stack_list[stack_idx].append(crate) # append stack to list
                
            
def move_crate(stcks: list[chr], amount:int, src:int, to:int) -> None:
    stcks[to].extend(stcks[src][-amount:]) # add sublist to list in reverse order (lifo)
    stcks[src] = stcks[src][:-amount] # remove sublist from src

f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")
stacks = list(map(lambda x: list(filter(lambda y: y != ' ', x)), get_stacks(puzzle_input))) # gets stacks and filters empty crates

for move_idx in range(len(stacks)+1, len(puzzle_input)): # iterates through move instructions
    move = puzzle_input[move_idx].split(" ")
    inst = [int(move[i]) for i in range(1, len(move), 2)] # gets instruction list [amount, from, to]
    move_crate(stacks, inst[0], inst[1]-1, inst[2]-1) # moves crate in stack
    

result = "".join([s[-1] for s in stacks if len(s) > 0]) # joins each element on top of stack in list

print(result) 