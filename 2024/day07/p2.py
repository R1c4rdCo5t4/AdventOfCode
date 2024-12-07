from equations import *

equations = parse_equations()
operators = "+*|" # add, multiply and concatenate
total = 0

for result, nums in equations.items():
    if is_equation_possible(result, nums, operators):
        total += result

print(total) # 189207836795655