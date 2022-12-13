

def parse_input() -> list[str]:
    f = open("puzzle_input.txt", "r")
    return f.read().splitlines()

def parse_packets(lines: list[str]) -> list[list]:
    packets = []
    for line in lines:
        if(line != ""):
            packets.append(parse_list(line))
        
    return packets


def parse_list(s):
    if not s:
        return []

    if s[0] != '[' or s[-1] != ']':
        return int(s)

    result = []
    start = 1
    depth = 0

    def add_sublist(start, end):
        result.append(parse_list(s[start:end]))

    for i in range(1, len(s) - 1):
        match(s[i]):
            case '[':
                depth += 1
            case ']':
                depth -= 1
            case ',':
                if depth == 0:
                    add_sublist(start, i)
                    start = i + 1

    add_sublist(start, -1)
    return result


def cmp_lists(left: list, right: list) -> int:
    for val in map(cmp_values, left, right):
        if val:
            return val
    return cmp_values(len(left), len(right))


def cmp_values(left: int | list, right: int | list) -> int:
    
    match left, right:
        case int(), int(): return (left < right) - (left > right) # 1 if in order, -1 if not, 0 if equal
        case int(), list(): return cmp_values([left], right)
        case list(), int(): return cmp_values(left, [right])
        case list(), list(): return cmp_lists(left, right)

