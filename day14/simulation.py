from dataclasses import dataclass, field
from typing import Callable
from time import sleep


position = tuple[int, int] # type alias


def parse_rocks() -> list[position]:
    f = open("puzzle_input.txt", "r")
    rocks = set()

    for line in f.read().splitlines():
        coords = line.split(" -> ")
        for i in range(len(coords)-1):
         
            x1, y1 = map(int, coords[i].split(","))
            x2, y2 = map(int, coords[i+1].split(","))
            rocks.add((x1, y1))
            
            if x1 == x2: # vertical
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    rocks.add((x1, y))
        
            else: # horizontal
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    rocks.add((x, y1))
                    
        x, y = map(int, coords[i+1].split(","))
        rocks.add((x, y))

    return rocks


def get_value(func: Callable[[list], int], lst: list, i:int) -> int:
    return func(lst, key=lambda k: k[i])[i] 


@dataclass
class Simulation:
    start: position
    rocks: set[position]
    sand: set[position] = field(default_factory=set)
    offset = (1,1)
    directions = ((0, 1), (-1, 1), (1, 1))


    @property
    def width(self):
        return max(self.rocks, key=lambda k: k[0])[0] +1

    @property
    def height(self):
        return max(self.rocks, key=lambda k: k[1])[1] +1 

    @property
    def min_x(self):
        return get_value(min, self.rocks, 0)
        
    @property
    def relative_height(self):
        return self.height + self.offset[1]

    @property
    def relative_width(self):
        return self.width - self.min_x + self.offset[0]


    def get_position(self, x:int, y:int) -> position:
        return (x+self.min_x, y)

     
    # counts rest sand units until one falls into the void
    def simulate_p1(self):
        sand_units = 0

        while True: # void
            curr_pos = self.start
   
            while True:
                if curr_pos[1] >= self.height: # reached max height
                    return sand_units
                    
                for dx, dy in self.directions: # move
                    next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
                    if next_pos not in self.rocks | self.sand:
                        curr_pos = next_pos
                        break

                else: # rest
                    self.sand.add(curr_pos)
                    sand_units += 1
                    break
                   
                # self.visualize()
                # sleep(0.1)
      
     
    # counts rest sand units until overflow, with infinitely wider ground
    def simulate_p2(self):
        sand_units = 0

        while True:
            curr_pos = self.start

            while True:
                if (curr_pos[1] >= self.height): # floor
                    sand_units += 1
                    self.sand.add(curr_pos)
                    break
                
                for dx, dy in self.directions: # move
                    next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
                    if next_pos not in self.rocks | self.sand:
                        curr_pos = next_pos
                        break
                
                else: # rest
                    sand_units += 1
                    self.sand.add(curr_pos)

                    if curr_pos == self.start:
                        return sand_units
                    break
                

                # self.visualize()
                # sleep(0.01)



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