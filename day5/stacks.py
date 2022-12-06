
def parse_stacks(input_lines: list[str]) -> list[chr] | None:
    stack_list = [] # list to store all stacks
    for stack_idx, line in enumerate(input_lines):
        stack_list.append([]) # create list for next stack

        for i in range(1,len(line), 4):
            crate = line[i]
            if(crate == '1'): # finished reading stacks
                stack_list.pop() # remove empty list
                stck = [list(map(str, col))[::-1] for col in zip(*stack_list)] # get stack collumns in reverse order (stack top in the end of list)
                return list(map(lambda sublst: list(filter(lambda elem: elem != ' ', sublst)), stck)) # gets stacks and filters empty crates   
            
            stack_list[stack_idx].append(crate) # append stack to list

            
def rearrange_stacks(stack_list : list[list[str]], puzzle_input: list[str], move_crates) -> None:
    for move_idx in range(len(max(stack_list, key=len))+2, len(puzzle_input)): # iterates through move instructions
        move = puzzle_input[move_idx].split(" ")
        _amount, _from, _to = [int(move[i]) for i in range(1, len(move), 2)] # gets instruction list [amount, from, to]
        move_crates(stack_list, _amount, _from - 1, _to - 1) # moves crate in stack
    

def get_stack_tops(stcks: list[str]):
    return "".join([s[-1] for s in stcks if len(s) > 0]) # joins each element on top of stack in list