from crt import *

ops = parse_input()
register = 1
cycle = 0
crt_pos = 0
crt_screen = ""
sprite = "###....................................."

def clock_cycle():
    global cycle
    global crt_screen
    global crt_pos

    cycle += 1
    crt_screen += sprite[crt_pos]
    crt_pos += 1
    
    if (check_new_line(cycle)):
        crt_screen += "\n"
        crt_pos = 0


for op in ops:
    clock_cycle()

    if op.name == "addx":
        clock_cycle()

        register += op.value
        sprite = shift_chars(sprite, op.value)
        

print(crt_screen) # PLGFKAZG

