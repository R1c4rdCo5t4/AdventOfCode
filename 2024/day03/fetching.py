def fetching(char: str, num1: int, num2: int) -> bool: # keep fetching?
    mul = 0
    if char not in [",", ")"] and not char.isdigit():
        return False, "", "", mul

    if type(num1) == str and char.isdigit():
        num1 += char

    elif char == ",":
        num1 = int(num1)

    elif char.isdigit():
        num2 += char

    elif char == ")":
        num2 = int(num2) if num2.isdigit() else 0
        if type(num1) == type(num2) == int:
            mul = num1 * num2

        return False, "", "", mul
    
    return True, num1, num2, mul