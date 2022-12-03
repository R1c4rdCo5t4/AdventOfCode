

f = open("puzzle_input.txt", "r")
puzzle_input = f.read()

priority_sum = 0
for line in puzzle_input.split("\n"):
    middle = int(len(line)/2)
    first = line[:middle]
    second = line[middle:]

    for item in second:
        if item in first:
            priority_sum += ord(item) - (96 if(ord(item) in range(ord('a'), ord('z')+1)) else 38)
            break           

print(priority_sum)