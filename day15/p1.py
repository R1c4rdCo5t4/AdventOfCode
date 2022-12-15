from sensors import parse_sensors

sensors = parse_sensors()

y = 2000000
intervals = []
x_positions = set()

for sensor in sensors:
    bx, by = sensor.closest_beacon
    dx = sensor.dist_to_closest_beacon - abs(sensor.pos.y - y)

    if dx > 0:
        intervals.append((sensor.pos.x - dx, sensor.pos.x + dx))
    if by == y:
        x_positions.add(bx)


min_x = min([i[0] for i in intervals])
max_x = max([i[1] for i in intervals])

pos_count = 0
for x in range(min_x, max_x + 1):
    if x not in x_positions and any(min_x <= x <= max_x for min_x, max_x in intervals):
        pos_count += 1

print(pos_count) # 4725496
