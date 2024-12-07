from equations import *

equations = parse_equations()
operators = "+*" # add and multiply
total = 0

for result, nums in equations.items():
    if is_equation_possible(result, nums, operators):
        total += result

print(total) # 1708857123053