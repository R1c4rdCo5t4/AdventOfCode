from dataclasses import dataclass

@dataclass
class Operation:
    name : str
    value : int


def parse_input():
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()

    return [Operation(inst[0], int(inst[1])) if(inst := line.split(" "))[0] == "addx" 
            else Operation(inst[0], None) for line in lines]


def check_signal_strength(cycles: int, register:int):
    if cycles == 20 or ((cycles+20) % 40) == 0:
        print(cycles, register, cycles * register)
        return cycles * register

    return 0