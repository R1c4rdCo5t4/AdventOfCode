from packets import *

lines = parse_input()
packets = parse_packets(lines)

right_sum = 0
count = 0
for idx in range(0, len(packets), 2):

    left, right = packets[idx], packets[idx + 1]
    count += 1
    if cmp_values(left, right) == 1:
        right_sum += count

print(right_sum) # 5366
