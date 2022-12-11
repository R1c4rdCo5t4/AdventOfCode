from dataclasses import dataclass

@dataclass
class Monkey:
    id: int
    items: list[int]
    op: str
    test: int
    true: int
    false: int
    inspect_count: int = 0

    @property
    def first(self) -> int:
        return self.items[0]
   
    def test_worry_level(self) -> bool:
        return (self.first % self.test) == 0
   
    def operation(self) -> int:
        op, value = self.op.split(" ")
        old = self.first
        operand = old if (value == "old") else int(value)
        result = old + operand if(op == '+') else old * operand
        self.items[0] = result
        return result

    @staticmethod
    def get_monkey_business(monkeys):
        two_most_active = sorted(monkeys, key=lambda m: m.inspect_count, reverse=True)[:2]
        monkey_business = two_most_active[0].inspect_count * two_most_active[1].inspect_count
        return monkey_business


def parse_input() -> list[Monkey] :
    f = open("puzzle_input.txt", "r")
    monkey_lines = f.read().split("\n\n")
    monkeys : list[Monkey] = []

    for monkey in monkey_lines:
        each = monkey.split("\n")
        id = each[0][7:].rstrip(":")
        starting_items = [int(it) for it in each[1][18:].split(", ")]
        operation =  each[2][23:]
        test = int(each[3][21:])
        true = int(each[4][29:])
        false = int(each[5][30:])

        monkeys.append(Monkey(id, starting_items, operation, test, true, false))
        
    return monkeys



