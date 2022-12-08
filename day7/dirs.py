from dataclasses import dataclass, field

@dataclass
class Directory:
    size : int = 0
    subdirs : list = field(default_factory=list)


def get_path(current_path, dir):
    parent_path = current_path if current_path != "/" else ""
    return f"{parent_path}/{dir}"

def compute_dir_size(dir_name, dirs):
    return dirs[dir_name].size + sum([compute_dir_size(subdir, dirs) for subdir in dirs[dir_name].subdirs])