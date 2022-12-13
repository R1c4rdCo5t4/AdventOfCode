

def parse_input() -> list[str]:
    f = open("puzzle_input.txt", "r")
    return f.read().splitlines()


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


def parse_lists(lines: list[str]) -> list[tuple[list,list]]:
    return [(parse_list(lines[idx]), parse_list(lines[idx+1])) for idx in range(0, len(lines), 3)]


def cmp_lists(left: list, right: list) -> int:
    for cmp_val in map(cmp_values, left, right):
        if cmp_val:
            return cmp_val
    return cmp_values(len(left), len(right))


def cmp_values(left: int | list, right: int | list) -> int:
    
    match left, right:
        case int(), int(): return (left < right) - (left > right) # 1 if in order, -1 if not, 0 if equal
        case int(), list(): return cmp_values([left], right)
        case list(), int(): return cmp_values(left, [right])
        case list(), list(): return cmp_lists(left, right)

    




        
