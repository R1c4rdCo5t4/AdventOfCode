from monkeys import *

monkeys = parse_input()
rounds = 10000
worry_level_div = 1

for _ in range(rounds):
    for monkey in monkeys: # each round
        while len(monkey.items) > 0:
            monkey.operation()
            if monkey.test_worry_level(worry_level_div):
                monkeys[monkey.true].items.append(monkey.items[0])
            else:
                monkeys[monkey.false].items.append(monkey.items[0])

            monkey.inspect_count += 1
            monkey.items = monkey.items[1:]


two_most_active = sorted(monkeys, key=lambda m: m.inspect_count, reverse=True)[:2]
monkey_business = two_most_active[0].inspect_count * two_most_active[1].inspect_count
print(monkey_business)
