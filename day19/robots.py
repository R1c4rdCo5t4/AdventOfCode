import re
from dataclasses import dataclass, field
from copy import deepcopy



# @dataclass
# class Robot:
#     costs: Resource

#     def __init__(self, ore_cost=0, clay_cost=0, obsidian_cost=0):
#         self.costs(ore_cost, clay_cost, obsidian_cost)

@dataclass
class Resource():
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __getitem__(self, idx:int) -> int:

        match idx:
            case 0:
                return self.ore
            case 1:
                return self.clay
            case 2:
                return self.obsidian
            case 3:
                return self.geode
            case _:
                raise IndexError("Invalid index")

    def __setitem__(self, idx:int, value:int) -> int:

        match idx:
            case 0:
                self.ore = value
            case 1:
                self.clay = value
            case 2:
                self.obsidian = value
            case 3:
                self.geode = value
            case _:
                raise IndexError("Invalid index")

    def __len__(self):
        return 4



@dataclass
class Blueprint:
    id: int
    costs: list[Resource] 
    # ore_robots: int = 1
    # clay_robots: int = 0
    # obsidian_robots: int = 0
    # geode_robots: int = 0
    robots : list[int]



def parse_blueprints():
    f = open("day19/puzzle_input.txt")
    lines = f.read().splitlines()
    f.close()

    blueprints = []
    for line in lines:
        id, orerc, clayrc, obsroc, obsrcc, geororec, georobsc = map(int, re.findall(r"\d+", line))
        blueprints.append(Blueprint(id, 
            [Resource(ore=orerc),
            Resource(ore=clayrc), 
            Resource(ore=obsroc, clay=obsrcc),
            Resource(ore=geororec, obsidian=georobsc)],
            [1,0,0,0]
        ))

    return blueprints



def next_robot_to_build(gains, costs):
    next_robot = 0
    if gains[0] >= costs[1][0] and gains[1] >= costs[1][1]:
        next_robot = 1
    elif gains[0] >= costs[2][0]:
        next_robot = 2
    elif gains[0] >= costs[3][0] and gains[1] >= costs[3][1] and gains[2] >= costs[3][2]:
        next_robot = 3
    return next_robot



def get_max_geodes(blueprints:list[Blueprint], time_limit:int):

    max_geodes = 0
    for b in blueprints:
        print("Blueprint", b.id)
        gains = [0,0,0,0]
        for min in range(1, time_limit+1):
            print("\n---Minute",min,"---")

            robot_built = None
            next_robot = next_robot_to_build(gains, b.costs)

            # build next robot if possible
            gc = list(zip(gains, b.costs[next_robot]))
            if all(g >= c for g,c in gc):
            
                tmp_cost = 0
                for j in range(len(b.costs[next_robot])):
                    gains[j] -= b.costs[next_robot][j]
                    tmp_cost += b.costs[next_robot][j]
                
                print(f"Spent {tmp_cost} to start building robot {next_robot}")
                robot_built = next_robot
                    
                    
            # collect resources
            for i,r in enumerate(b.robots):
                # print(gains[i], r)
                gains[i] += r
                if r > 0:
                    print(f"robot {i} collecting, now have {gains[i]}")
                
            # print(gains)
            if robot_built:
                b.robots[robot_built] += 1
                print(f"new robot {i} is ready, now have {b.robots[i]} of them")


        # get max number of geodes collected
        max_geodes = max(max_geodes, gains[3])
      
    return max_geodes


blueprints = parse_blueprints()

ans = get_max_geodes([blueprints[1]], 24)
print(ans)
