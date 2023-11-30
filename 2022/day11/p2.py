from monkeys import *
import math

Monkey.monkeys = parse_input()
rounds = 10000
lcm = math.lcm(*[monkey.test for monkey in Monkey.monkeys])

for _ in range(rounds):
    for monkey in Monkey.monkeys: # each round
        while len(monkey.items) > 0:
            monkey.operation()
            monkey.items[0] = monkey.first % lcm
            monkey.throw()

monkey_business = Monkey.get_monkey_business()
print(monkey_business) # 20151213744
