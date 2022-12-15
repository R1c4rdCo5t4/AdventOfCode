from simulation import *


rocks = parse_rocks()
sand_start = (500, 0)
sim = Simulation(sand_start, rocks)
units = sim.simulate_p1()

print(units) # 644
