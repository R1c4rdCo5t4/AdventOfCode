

from ropes import *


moves = parse_input()
starting_pos = (0,0)

total_nodes = 10
nodes = [starting_pos for _ in range(10)]
tail_positions = {starting_pos}

# head = nodes[0]
# tail = nodes[1:]  

for dir, val in moves:
    direction = get_move_direction(dir)
    for _ in range(val):
        nodes[0] = move_node(nodes[0], direction)

        for i in range(1, len(nodes)): # move tail
            nodes[i] = update_tail(nodes[i - 1], nodes[i])
            
        tail_positions.add(nodes[-1])
        

print(len(tail_positions)) # 2724
