from crt import *

ops = parse_input()
register = 1
cycles = 0
signal_strength_sum = 0

def clock_cycle():
    global cycles
    global signal_strength_sum
    global register
    
    cycles += 1
    signal_strength_sum += check_signal_strength(cycles, register)


for op in ops:
    clock_cycle()
    if op.name == "addx":
        clock_cycle()
        register += op.value
        

print(signal_strength_sum) # 15880

