from dataclasses import dataclass, field
from typing import TextIO


@dataclass
class Directory:
    size : int = 0
    subdirs : list["Directory"] = field(default_factory=list)


def get_path(current_path : str, dir: str) -> str:
    if current_path == "":
        return dir
    else:
        parent_path = current_path if current_path != "/" else ""
        return f"{parent_path}/{dir}"



def compute_dir_size(dir: str | Directory, dirs: dict[str, Directory]) -> int:
    return dirs[dir].size + sum([compute_dir_size(subdir, dirs) for subdir in dirs[dir].subdirs])


def parse_directories(f: TextIO) -> dict[str, Directory]:

    get_next_line = lambda f: f.readline().rstrip("\n")
    dirs : dict[str, Directory] = {}
    current_path = ""

    while(line := get_next_line(f)) != "":
        if line.startswith('$'): # command

            if line.startswith('$ cd'): # cd
                dir = line.split(" ")[2]
                if dir == "..": # remove the last dir from the path
                    if current_path != "/":
                        path_split = current_path.rsplit("/", 1)
                        if path_split:
                            current_path = path_split[0] if(current_path.count('/') > 1) else "/"
                
                else: # add the dir to the path
                    current_path = get_path(current_path, dir)

            else: # ls setup
                dirs[current_path] = Directory()

        else: # ls execution
            val, name = line.split(" ")
            if val == "dir": # directory
                path = get_path(current_path, name)
                dirs[current_path].subdirs.append(path)

            else: # file
                dirs[current_path].size += int(val)      
    
    return dirs