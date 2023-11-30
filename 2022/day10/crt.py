from dataclasses import dataclass
from math import copysign


@dataclass
class Operation:
    name : str
    value : int | None


def parse_input() -> list[Operation]:
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()

    return [Operation(inst[0], int(inst[1])) 
            if(inst := line.split(" "))[0] == "addx" 
            else Operation(inst[0], None) for line in lines]


def get_signal_strength(cycles: int, register:int) -> int:
    if cycles == 20 or ((cycles + 20) % 40) == 0:
        return cycles * register

    return 0


def check_new_line(cycles: int) -> bool:
    return cycles % 40 == 0
    
        
def shift_chars(string:str, amount:int):
    sign = -int(copysign(1, amount))
    for _ in range(abs(amount)):
        string = string[sign:] + string[:sign]
    
    return string


