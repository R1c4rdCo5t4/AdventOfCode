from dataclasses import dataclass, field

@dataclass
class Directory:
    size : int = 0
    subdirs : list["Directory"] = field(default_factory=list)


def get_path(current_path, dir):
      
    if current_path == "":
        return dir
   
    else:
        parent_path = current_path if current_path != "/" else ""
        return f"{parent_path}/{dir}"

def compute_dir_size(dir: str, dirs: dict[str, Directory]) -> int:
    return dirs[dir].size + sum([compute_dir_size(subdir, dirs) for subdir in dirs[dir].subdirs])

def get_next_line(file):
    return file.readline().rstrip("\n")

def parse_directories(f) -> dict[str, Directory]:

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
    
    return dirs