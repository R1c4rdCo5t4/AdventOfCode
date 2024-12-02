with open("puzzle_input.txt") as f:
    pairs = [list(map(int, line.split("   "))) for line in f.read().splitlines()]
    fst_list = sorted([n[0] for n in pairs])
    snd_list = sorted([n[1] for n in pairs])

    result = 0
    for i in range(0, len(fst_list)):
        result += abs(fst_list[i] - snd_list[i])

    print(result) # 1879048

