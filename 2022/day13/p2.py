from packets import *
from functools import cmp_to_key

lines = parse_input()
divider_packets = [[2]] + [[6]]
packets = divider_packets + parse_packets(lines)

packets.sort(key=cmp_to_key(cmp_values), reverse=True)
packet_index = lambda p: packets.index(p) + 1
decoder_key = packet_index(divider_packets[0]) * packet_index(divider_packets[1])

print(decoder_key) # 23391
