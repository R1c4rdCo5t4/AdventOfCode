from dataclasses import dataclass
import re

@dataclass()
class Position:
    x: int
    y: int

    def __iter__(self):
        yield self.x
        yield self.y


@dataclass
class Sensor:
    pos: Position
    closest_beacon: Position

    def __init__(self, sx:int, sy:int, bx:int, by:int):
        self.pos = Position(sx,sy)
        self.closest_beacon = Position(bx, by)

    @property
    def dist_to_closest_beacon(self) -> int:
        return manhattan_dist(self.pos, self.closest_beacon)



def manhattan_dist(pos1:Position, pos2:Position) -> int:
    return abs(pos1.x -pos2.x) + abs(pos1.y - pos2.y)


def parse_sensors():
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    sensors = []

    for line in lines:
        x1, y1, x2, y2 = map(int, re.findall(r"-?\d+", line))
        sensors.append(Sensor(x1, y1, x2, y2))

    return sensors



def calc_edge_range(sensor: Sensor, row: int) -> tuple[int, int]:
    sx, sy = sensor.pos
    diff =  sensor.dist_to_closest_beacon - abs(row - sy)
    if diff < 0: # the beacon isnt within the sensor's range in the row
        return None

    return sx-diff, sx+diff
    

def detect_edges(sensors: list[Sensor], row: int) -> list[tuple[int, int]]:
    all_edges = [calc_edge_range(sensor, row) for sensor in sensors]
    return sorted([edge for edge in all_edges if edge is not None])



def find_gap(edges):
    highest = 0
    
    for a, b in edges:
        if a <= highest + 1:
            highest = max(b, highest)
        else:
            return a - 1
            
    return None