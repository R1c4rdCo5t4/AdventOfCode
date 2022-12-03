
# Strategy Guide:
#   X -> lose
#   Y -> draw
#   Z -> win


f = open("puzzle_input.txt", "r")
puzzle_input = f.read()


# outcome: (outcome points, index-based play score)
possible_plays = {
    'X': (0, ['B', 'C', 'A']), #  losing
    'Y': (3, ['A', 'B', 'C']), #  drawing
    'Z': (6, ['C', 'A', 'B'])  #  winning
}

score = 0
for input_line in puzzle_input.split("\n"):

    plays = input_line.split(" ")
    opponent_play = plays[0]
    outcome = plays[1]
    play = possible_plays[outcome]
    score += play[0] + play[1].index(opponent_play) + 1


print(score) # 11756
