from valves import *

valves = parse_valves()

minutes = 0
max_minutes = 30
curr_valve = valves[0]


while minutes < max_minutes:
    minutes += 1

    cost = curr_valve.flow_rate

    if curr_valve: # release valve
        pass

    else: # open valve
        max()


