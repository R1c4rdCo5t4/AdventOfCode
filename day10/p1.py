from cpu import *

ops = parse_input()
register = 1
cycles = 0
signal_strength_sum = 0
for op in ops:

    cycles += 1
    signal_strength_sum += check_signal_strength(cycles, register)

    if op.name == "addx":
        cycles += 1
        signal_strength_sum += check_signal_strength(cycles, register)
        register += op.value
        

print(signal_strength_sum) # 15880

