from dataclasses import dataclass

@dataclass
class Monkey:
    items: list[int]
    op: str
    test: int
    true: int
    false: int
    inspect_count: int = 0
    monkeys = list["Monkey"]

    @property
    def first(self) -> int:
        return self.items[0]
   
    @property
    def test_worry_level(self) -> bool:
        return (self.first % self.test) == 0
   

    def operation(self) -> int:
        op, value = self.op.split(" ")
        old = self.first
        operand = old if (value == "old") else int(value)
        result = old + operand if(op == '+') else old * operand
        self.items[0] = result
        return result


    def throw(self) -> None:
        self.inspect_count += 1
        target_monkey = self.true if self.test_worry_level else self.false
        self.monkeys[target_monkey].items.append(self.first) 
        self.items = self.items[1:]
        

    @staticmethod
    def get_monkey_business():
        two_most_active = sorted(Monkey.monkeys, key=lambda m: m.inspect_count, reverse=True)[:2]
        monkey_business = two_most_active[0].inspect_count * two_most_active[1].inspect_count
        return monkey_business

  



def parse_input() -> list[Monkey] :
    f = open("puzzle_input.txt", "r")
    monkey_lines = f.read().split("\n\n")
    monkeys : list[Monkey] = []

    for monkey in monkey_lines:
        each = monkey.split("\n")
        starting_items = [int(it) for it in each[1][18:].split(", ")]
        operation =  each[2][23:]
        test = int(each[3][21:])
        true = int(each[4][29:])
        false = int(each[5][30:])

        monkeys.append(Monkey(starting_items, operation, test, true, false))
        
    return monkeys



