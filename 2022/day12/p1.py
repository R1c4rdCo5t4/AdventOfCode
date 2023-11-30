from graph import *


lines = parse_input()
start, end = get_start_and_end(lines)
graph = Graph.build(lines)
steps = graph.BFS(start, end)

print(steps) # 528

