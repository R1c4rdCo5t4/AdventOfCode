

class Number:
    def __init__(self, val: int):
        self.val = val

    def __mul__(self, other):
        self.val *= other  
        return self 
        

def parse_input() -> list[Number]:
    f = open('puzzle_input.txt', 'r')
    numbers = [Number(int(line)) for line in f.read().splitlines()]
    f.close()
    return numbers


def mix_numbers(numbers:list[Number], times:int=1, factor:int=1):

    unchanged = [i * factor for i in numbers]
    numbers_len = len(numbers)
    for _ in range(times):
        for item in unchanged:
            curr_idx = numbers.index(item)
            shift = abs(item.val) % (numbers_len - 1)
            if item.val < 0:
                shift = -shift

            next_idx = curr_idx + shift
            if next_idx >= numbers_len:
                next_idx = (next_idx % numbers_len) + 1
            elif next_idx == 0:
                next_idx = numbers_len if shift < 0 else 0 

            numbers.insert(next_idx, numbers.pop(curr_idx))

