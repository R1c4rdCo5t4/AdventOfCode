from crt import *


def clock_cycle():
    global cycle, signal_strength_sum, register
    cycle += 1
    signal_strength_sum += get_signal_strength(cycle, register)

ops = parse_input()
register = 1
cycle = 0
signal_strength_sum = 0

for op in ops:
    clock_cycle()
    if op.name == "addx":
        clock_cycle()
        register += op.value
        

print(signal_strength_sum) # 15880

