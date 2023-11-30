from graph import *
from math import inf


lines = parse_input()
_, end = get_start_and_end(lines)
graph = Graph.build(lines)

lowest_starts = [v for x, y in graph.graph if (v:=Vertex((x,y),lines[y][x])).altitude == 0]
min_steps = inf

for start in lowest_starts:
    steps = graph.BFS(start, end)
    if steps != -1 and steps < min_steps:
        min_steps = steps

print(min_steps) # 522