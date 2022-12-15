from dataclasses import dataclass, field
from typing import Callable
from time import sleep


position = tuple[int, int] # type alias


def parse_input() -> list[list[position]]:
    f = open("puzzle_input.txt", "r")
    result = []
    for idx, line in enumerate(f.read().splitlines()):
        result.append([])
        for coord in line.split(" -> "):
            x, y = map(int, coord.split(","))
            result[idx].append((x,y))

    return result



def get_rocks(scans: list[list[position]]):
    points = []

    for scn in scans:
        points.extend(scn)
        
        for i in range(0, len(scn)-1):  
            x1, y1 = scn[i]
            x2, y2 = scn[i+1]

            if x1 == x2: # vertical
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    points.append((x1, y))

            else: # horizontal
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    points.append((x, y1))

    return points



def get_value(func: Callable[[list], int], lst: list, i:int) -> int:
    return func(lst, key=lambda k: k[i])[i] 


@dataclass
class Simulation:
    start: position
    rocks: list[position]
    sand: list[position] = field(default_factory=list)
    offset = (1,1)
    directions = ((0, 1), (-1, 1), (1, 1))

    @property
    def width(self):
        return get_value(max, self.rocks, 0) + 1

    @property
    def height(self):
        return get_value(max, self.rocks, 1) + 1

    @property
    def min_x(self):
        return get_value(min, self.rocks, 0)
        
    @property
    def min_y(self):
        return get_value(min, self.rocks, 1)
    
    @property
    def relative_height(self):
        return self.height + self.offset[1]

    @property
    def relative_width(self):
        return self.width - self.min_x + self.offset[0]


    def get_position(self, x:int, y:int) -> position:
        return (x+self.min_x, y)


    def visualize(self):
        # print("\033[2J") # clear screen
        print("\033[H") # move cursor to the top-left

        for y in range(self.relative_height):
            print('.', end="")
            for x in range(self.relative_width):
                pos = self.get_position(x,y)
                char = '.'
                if(pos == self.start):
                    char = '+'
                elif(pos in self.rocks):
                    char = '#'
                elif(pos in self.sand):
                    char = 'O'
                
                print(char, end='\n' if x == self.relative_width-1 else '')
       
         
    # counts rest sand units until one falls into the void
    def simulate_p1(self):
        sand_units = 0

        while True: # void
            curr_pos = self.start
            self.sand.append(curr_pos)
   
            while True:
                if curr_pos[1] >= self.height:
                    return sand_units
                    
                for dx, dy in self.directions:
                    next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
                    if not any(next_pos in pos for pos in [self.rocks, self.sand]):
                        curr_pos = next_pos
                        self.sand[sand_units] = curr_pos
                        break

                else: # rest
                    self.sand[sand_units] = curr_pos
                    sand_units += 1
                    break
                   
                self.visualize()
                # sleep(0.01)
      
     
    # counts rest sand units until overflow, with infinitely wider ground
    def simulate_p2(self):
        sand_units = 0

        while True: # void
            curr_pos = self.start
            self.sand.append(curr_pos)

            left = (curr_pos[0] - 1, curr_pos[1] + 1)
            middle = (curr_pos[0], curr_pos[1] + 1)
            right = (curr_pos[0] + 1, curr_pos[1] + 1)

            if all(x in self.sand for x in [left,middle,right]): # overflow
                return sand_units + 1

            while True:
                for dx, dy in self.directions:
                    next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
                    if not any(next_pos in pos for pos in [self.rocks, self.sand]):
                        curr_pos = next_pos
                        self.sand[sand_units] = curr_pos
                        break
                
                else: # rest
                    self.sand[sand_units] = curr_pos 
                    sand_units += 1
                    break
                   
                if (curr_pos[1] >= self.height): # floor
                    self.sand[sand_units] = curr_pos
                    sand_units += 1
                    break
                   
                self.visualize()
                # sleep(0.01)
