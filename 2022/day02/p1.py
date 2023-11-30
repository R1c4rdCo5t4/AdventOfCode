
# strategy guide:
#   X -> rock
#   Y -> paper
#   Z -> scissors

f = open("puzzle_input.txt", "r")
puzzle_input = f.read().split("\n")

play_dict = {
    'A':'X',
    'B':'Y',
    'C':'Z'
}

winning_plays = [['A','Y'], ['B', 'Z'], ['C', 'X']]
score = 0

for input_line in puzzle_input:

    plays = input_line.split(" ")
    opponent_play = plays[0]
    my_play = plays[1]

    if(play_dict[opponent_play] == my_play): # draw
        score += 3

    elif([opponent_play, my_play] in winning_plays): # win
        score += 6

    score += list(play_dict.values()).index(my_play) + 1

   
print(score) # 12645

    
