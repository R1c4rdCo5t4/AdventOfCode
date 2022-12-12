from monkeys import *

Monkey.monkeys = parse_input()
rounds = 20
for _ in range(rounds):
    for monkey in Monkey.monkeys: # each round
        while len(monkey.items) > 0:
            monkey.operation()
            monkey.items[0] //= 3 
            monkey.throw()

monkey_business = Monkey.get_monkey_business()
print(monkey_business) # 58794
