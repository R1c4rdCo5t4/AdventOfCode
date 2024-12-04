from fetching import fetching

with open("puzzle_input.txt") as f:
    text = f.read()
    num1, num2 = "", ""
    fetch = False
    do = True
    mul_str = "mul("
    do_str = "do()"
    dont_str = "don't()"
    result = 0
    i = 0
    while i < len(text):
        char = text[i]

        if fetch and do:   
            fetch, num1, num2, mul = fetching(char, num1, num2)
            result += mul

        if text[i:i+len(mul_str)] == mul_str:    
            fetch = True
            i += len(mul_str)

        elif text[i:i+len(dont_str)] == dont_str:
            do = False
            i += len(dont_str)

        elif text[i:i+len(do_str)] == do_str:
            do = True
            i += len(do_str)

        else:
            i += 1
            
    print(result) # 59097164
    