from fetching import fetching

with open("puzzle_input.txt") as f:
    text = f.read()
    num1, num2 = "", ""
    fetch = False
    do = True
    mul_len = len("mul(")
    do_len = len("do()")
    dont_len = len("don't()")
    result = 0
    i = 0
    while i < len(text):
        char = text[i]

        if fetch and do:   
            fetch, num1, num2, mul = fetching(char, num1, num2)
            result += mul

        if text[i:i+mul_len] == "mul(":    
            fetch = True
            i += mul_len

        elif text[i:i+dont_len] == "don't()":
            do = False
            i += dont_len

        elif text[i:i+do_len] == "do()":
            do = True
            i += do_len

        else:
            i += 1
            
    print(result) # 59097164
    