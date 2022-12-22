from monkey_math import *
from sympy import symbols, solve_linear
   

monkeys = parse_input()
humn = symbols('humn')

first, _, second = monkeys['root']
left = calculate(first, monkeys, humn)
right = calculate(second, monkeys, humn)

yell = solve_linear(left, right)[1] # 3423279932937
print(yell)


