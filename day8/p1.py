
f = open("puzzle_input.txt", "r")
puzzle_input = f.read().splitlines()

count = 0
for line_idx, line in enumerate(puzzle_input):
    for col_idx, tree in enumerate(line):

        if line_idx not in range(1, len(puzzle_input)-1) or col_idx not in range(1, len(line)-1): # edge trees
            count += 1  
            continue
        
        # inner trees
        t = int(tree)
        left = all(int(col) < t for col in line[:col_idx])
        right = all(int(col) < t for col in line[col_idx+1:])
        up = all(int(line) < t for line in [puzzle_input[i][col_idx] for i in range(line_idx)])
        down = all(int(line) < t for line in [puzzle_input[i][col_idx] for i in range(line_idx + 1, len(puzzle_input))])
            
        if any([left, right, up, down]):
            count += 1
   
               
print(count) # 1807
