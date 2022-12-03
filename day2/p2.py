
# Strategy Guide:
#   X -> lose
#   Y -> draw
#   Z -> win


f = open("puzzle_input.txt", "r")
puzzle_input = f.read()

#                     losing           drawing          winning
possible_plays = [['B', 'C', 'A'], ['A', 'B', 'C'], ['C', 'A', 'B']]

score = 0
for input_line in puzzle_input.split("\n"):

    plays = input_line.split(" ")
    opponent_play = plays[0]
    game_end = plays[1]

    match(game_end):
        case "X": # lose
            score += possible_plays[0].index(opponent_play) + 1

        case "Y": # draw
            score += possible_plays[1].index(opponent_play) + 4
            
        case "Z": # win
            score += possible_plays[2].index(opponent_play) + 7


print(score) # 11756

    
