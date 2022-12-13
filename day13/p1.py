from packets import *

lines = parse_input()
lists = parse_lists(lines)

right_sum = 0
for i, lst in enumerate(lists, 1):
    if cmp_values(lst[0], lst[1]) == 1:
        right_sum += i

print(right_sum) # 5366
