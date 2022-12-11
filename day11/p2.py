from monkeys import *
from math import lcm

monkeys = parse_input()
rounds = 10000
lmc = lcm(*[monkey.test for monkey in monkeys])

for _ in range(rounds):
    for monkey in monkeys: # each round
        while len(monkey.items) > 0:
            monkey.operation()
            monkey.items[0] = monkey.first % lmc

            if monkey.test_worry_level():
                monkeys[monkey.true].items.append(monkey.first)
            else:
                monkeys[monkey.false].items.append(monkey.first)

            monkey.inspect_count += 1
            monkey.items = monkey.items[1:]


monkey_business = Monkey.get_monkey_business(monkeys)
print(monkey_business) # 20151213744
