from dirs import *

def get_next_line(file):
    return file.readline().rstrip("\n")

f = open("puzzle_input.txt", "r")

max_dir_sum = 100000
dirs : dict[str, Directory] = {}
current_path = ""

while(line := get_next_line(f)) != "":

    if line.startswith('$'): # command
       
        if line.startswith('$ cd'): # cd
            _, cmd, dir = line.split(" ") 
            if dir == "..": # remove the last dir from the path
                if current_path != "/":
                    path_split = current_path.rsplit("/", 1)
                    if path_split:
                        current_path = path_split[0] if(current_path.count('/') > 1) else "/"
            else: # add the dir to the path
                current_path = get_path(current_path, dir)

        else: # ls
            dirs[current_path] = Directory()

    else: # ls execution
        val, name = line.split(" ")
        if val == "dir": # directory
            path = get_path(current_path, name)
            dirs[current_path].subdirs.append(path)

        else:  # file
            dirs[current_path].size += int(val)            

f.close()

result = 0
for dir in dirs.keys():
    dir_sum = compute_dir_size(dir, dirs)
    if dir_sum <= max_dir_sum:
        result += dir_sum


print(result) # 1297683
