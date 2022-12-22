from sympy import parse_expr


def parse_input():
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    f.close()

    monkey_dict = {}
    for line in lines:
        sp = line.split(" ")
        monkey = sp[0][:-1]
        yell = sp[1:]
        monkey_dict[monkey] = int(yell[0]) if len(yell) == 1 else yell

    return monkey_dict



def calculate(monkey: str, monkeys:dict[str, int | list], humn):
    if monkey == "humn":
        return humn

    if type(monkeys[monkey]) is int:
        return monkeys[monkey]

    operation = monkeys[monkey]
    first, op, second = operation

    left = calculate(first, monkeys, humn)
    right = calculate(second, monkeys, humn)

    return parse_expr(f"({left}){op}({right})")

    
 

        
