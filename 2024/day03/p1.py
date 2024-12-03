from fetching import fetching

with open("puzzle_input.txt") as f:
    text = f.read()
    num1, num2 = "", ""
    fetch = False
    result = 0
    i = 0
    while i < len(text):
        char = text[i]
        if fetch:   
            fetch, num1, num2, mul = fetching(char, num1, num2)
            result += mul

        if text[i:i+4] == "mul(":
            fetch = True
            i += 4
        else:
            i += 1

    print(result) # 183669043
