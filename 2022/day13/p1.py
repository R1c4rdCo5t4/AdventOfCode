from packets import *

lines = parse_input()
packets = parse_packets(lines)
right_sum = 0
idx = 0

for i in range(0, len(packets), 2):
    left, right = packets[i], packets[i + 1]
    idx += 1
    if cmp_values(left, right) == 1:
        right_sum += idx

print(right_sum) # 5366

