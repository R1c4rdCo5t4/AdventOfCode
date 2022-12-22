from monkey_math import *

   
monkeys = parse_input()
idx = 0

while(any(type(x) is list for x in monkeys.values())): # while not all monkeys have its value calculated
    monkey_key = list(monkeys.keys())[idx]
    monkey_value = monkeys[monkey_key]

    if type(monkey_value) is list:
        calculate(monkeys, monkey_key, monkey_value)

    idx = (idx+1) % len(monkeys.keys())

    
print(monkeys['root']) # 75147370123646



