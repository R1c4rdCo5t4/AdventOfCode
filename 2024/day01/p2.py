with open("puzzle_input.txt") as f:
    pairs = [list(map(int, line.split("   "))) for line in f.read().splitlines()]
    fst_list = [n[0] for n in pairs]
    snd_list = [n[1] for n in pairs]

    num_count = dict()
    for num in snd_list:
        if num not in num_count.keys():
            num_count[num] = 1
        else:
            num_count[num] += 1

    result = 0
    for num in fst_list:
        count = num_count[num] if num in num_count.keys() else 0
        result += num * count

    print(result) # 21024792

