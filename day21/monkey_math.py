
def parse_input():
    monkey_dict = {}
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    
    for line in lines:
        sp = line.split(" ")
        monkey = sp[0][:-1]
        yell = sp[1:]
        monkey_dict[monkey] = int(yell[0]) if len(yell) == 1 else yell

    return monkey_dict



def calculate(monkeys: dict[str, int | list], monkey: str, operation: list[str]) -> None:
    first, op, second = operation
    
    if type(monkeys[first]) is int and type(monkeys[second]) is int: # has values, can perform calculation
        first = int(monkeys[first])
        second = int(monkeys[second])
  
        match(op):
            case '+': monkeys[monkey] = first + second
            case '-': monkeys[monkey] = first - second
            case '*': monkeys[monkey] = first * second
            case '/': monkeys[monkey] = first // second
        
