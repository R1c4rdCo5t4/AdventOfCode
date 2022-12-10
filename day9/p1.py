from ropes import *


moves = parse_input()
head_pos = (0,0)
tail_pos = (0,0)
tail_positions = {tail_pos}


for dir, val in moves:
    direction = get_move_direction(dir)
    
    for _ in range(val):
        head_pos = move_node(head_pos, direction)
        tail_pos = update_tail(head_pos, tail_pos) 
        tail_positions.add(tail_pos) # add to set


print(len(tail_positions)) # 6503


