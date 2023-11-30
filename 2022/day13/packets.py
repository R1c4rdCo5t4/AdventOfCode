
def parse_input() -> list[str]:
    f = open("puzzle_input.txt", "r")
    return f.read().splitlines()


def parse_packets(lines: list[str]) -> list[list]:
    packets = []
    for line in lines:
        if(line != ""):
            packets.append(parse_list(line))
        
    return packets


def parse_list(line: str) -> list:
    if not line:
        return []

    if line[0] != '[' or line[-1] != ']':
        return int(line)

    result = []
    start = 1
    depth = 0

    def add_sublist(start, end):
        result.append(parse_list(line[start:end]))

    for idx in range(1, len(line) - 1):
        match line[idx]:
            case '[':
                depth += 1
            case ']':
                depth -= 1
            case ',':
                if depth == 0:
                    add_sublist(start, idx)
                    start = idx + 1

    add_sublist(start, -1)
    return result


def cmp_lists(left: list, right: list) -> int:
    for val in map(cmp_values, left, right):
        if val:
            return val
    return cmp_values(len(left), len(right))


def cmp_values(left: int | list, right: int | list) -> int:
    
    match left, right:
        case int(), int(): return (left < right) - (left > right) # 1 if in greater, 0 if equal, -1 if lower 
        case int(), list(): return cmp_values([left], right)
        case list(), int(): return cmp_values(left, [right])
        case list(), list(): return cmp_lists(left, right)

