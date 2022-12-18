from sensors import *

sensors = parse_sensors()
max_limit = 4000000
distress_beacon = None

for y in reversed(range(max_limit+1)):
    
    edges = detect_edges(sensors, y)
    x = find_gap(edges)
    
    if x: # gap was found
        distress_beacon = Position(x, y)
        break

tuning_freq = distress_beacon.x * max_limit + distress_beacon.y

print(tuning_freq) # 12051287042458
