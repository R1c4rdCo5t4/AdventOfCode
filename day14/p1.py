from simulation import *

scans = parse_input()
rocks = get_rocks(scans)

sand_start = (500, 0)
sim = Simulation(sand_start, rocks)
units = sim.simulate_p1()

print(units) # 644
