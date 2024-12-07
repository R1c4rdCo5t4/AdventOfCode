from typing import Generator

def parse_equations() -> dict[int, list[int]]:
    with open("puzzle_input.txt") as f:
        lines = f.read().splitlines()
        return  {int(line.split(": ")[0]): [int(num) for num in line.split(": ")[1].split(" ")] for line in lines}

def left_to_right_eval(nums: list[int], ops: str) -> int:
    """evaluates the expression from left to right using operators"""
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            result += nums[i+1]
        elif ops[i] == "*":
            result *= nums[i+1]
        elif ops[i] == "|":
            result = int(str(result) + str(nums[i + 1]))
    return result

def get_operator_combinations(n: int, ops: str, curr_combination: list[str]=[]):
    """brute forces all possibilities of operators: len(ops) ^ n"""
    if len(curr_combination) == n:
        yield curr_combination
    else:
        for op in ops:
            yield from get_operator_combinations(n, ops, curr_combination + [op])

def is_equation_possible(result: int, nums: list[int], ops: str) -> bool:
    """checks if the equation is possible"""
    positions = len(nums) - 1
    for ops in get_operator_combinations(positions, ops):
        if left_to_right_eval(nums, ops) == result:
            return True
    return False  