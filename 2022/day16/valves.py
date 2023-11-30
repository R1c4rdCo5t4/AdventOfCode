from dataclasses import dataclass
import re

@dataclass
class Valve:
    id: str
    flow_rate: int
    connected_valves: list[str]

    def __hash__(self):
        return hash((self.id, self.flow_rate, tuple(self.connected_valves)))

    def __eq__(self, other):
        if not isinstance(other, Valve):
            return False
        return (self.id, self.flow_rate, self.connected_valves) == (other.id, other.flow_rate, other.connected_valves)


def parse_valves() -> set[Valve]:
    f = open("puzzle_input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    valves = {}
    for line in lines:
        split = line.split(" ")
        valve_id = split[1]
        flow_rate = int(re.findall(r"\d+", line)[0])
        connected_valves = [x.rstrip(",") for x in split[9:]]

        valves[valve_id] = Valve(valve_id, flow_rate, connected_valves)
        
    return valves


def bfs():
    pass