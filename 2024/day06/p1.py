from map import *

data = get_puzzle_data()
visited_positions = walk(data)
print(len(visited_positions)) # 4973