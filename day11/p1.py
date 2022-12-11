from monkeys import *

monkeys = parse_input()
rounds = 20

for _ in range(rounds):
    for monkey in monkeys: # each round
        while len(monkey.items) > 0:
            monkey.operation()
            monkey.items[0] //= 3

            if monkey.test_worry_level():
                monkeys[monkey.true].items.append(monkey.first) 
            else:
                monkeys[monkey.false].items.append(monkey.first)

            monkey.inspect_count += 1
            monkey.items = monkey.items[1:]


monkey_business = Monkey.get_monkey_business(monkeys)
print(monkey_business) # 58794
