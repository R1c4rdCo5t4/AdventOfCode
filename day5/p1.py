import time

def get_stacks(input_lines: list[str]) -> list[chr] | None:
    stack_list = [] # list to store all stacks
    for stack_idx, line in enumerate(input_lines):
        stack_list.append([]) # create list for next stack

        for i in range(1,len(line), 4):
            crate = line[i]
            if(crate == '1'): # finished reading stacks
                stack_list.pop() # remove empty list
                stck = [list(map(str, col))[::-1] for col in zip(*stack_list)] # get stack collumns in reverse order (stack top in the end of list)
                return list(map(lambda x: list(filter(lambda y: y != ' ', x)), stck)) # gets stacks and filters empty crates   
            
            stack_list[stack_idx].append(crate) # append stack to list
                
            
def move_crate(stcks: list[chr], amount:int, src:int, to:int) -> None:
    stcks[to].extend(stcks[src][-1:-amount-1:-1]) # add sublist to list in reverse order (lifo)
    stcks[src] = stcks[src][:-amount] # remove sublist from src

import time

# Start the timer
start = time.perf_counter()

 
f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")
stacks = get_stacks(puzzle_input)

for move_idx in range(len(max(stacks, key=len))+2, len(puzzle_input)): # iterates through move instructions
    move = puzzle_input[move_idx].split(" ")
    _amount, _from, _to = [int(move[i]) for i in range(1, len(move), 2)] # gets instruction list [amount, from, to]
    move_crate(stacks, _amount, _from - 1, _to - 1) # moves crate in stack
    

result = "".join([s[-1] for s in stacks if len(s) > 0]) # joins each element on top of stack in list

print(result) # LBLVVTVLP

# Stop the timer
end = time.perf_counter()

# Calculate the elapsed time
elapsed = end - start
# Print the elapsed time
print("The algorithm took %.2f seconds to execute" % elapsed)