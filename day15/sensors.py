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
    def dist_to_closest_beacon(self):
        return manhattan_dist(self.pos, self.closest_beacon)



def manhattan_dist(pos1:Position, pos2:Position) -> int:
    return abs(pos1.x -pos2.x) + abs(pos1.y - pos2.y)


def parse_sensors():
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    sensors = []

    for line in lines:
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        sensors.append(Sensor(x1, y1, x2, y2))

    return sensors

