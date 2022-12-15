from sand import *


rocks = parse_rocks()
sand_start = (500, 0)
sim = Simulation(sand_start, rocks)
units = sim.simulate_p2()

print(units) # 27324
