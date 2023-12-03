with open("puzzle_input.txt") as file:
    lines = file.read().splitlines()

digits_dict: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

result = 0
for line in lines:
    
    def find_digit(reversed: bool = False) -> int:
        sort = -1 if reversed else 1
        word = ""
        for char in line[::sort]:
            if(char.isdigit()):
                return int(char)
                
            word += str(char)
            for digit_name in digits_dict:
                if reversed:
                    if word[::-1].startswith(digit_name) or word[::-1].endswith(digit_name):
                        return digits_dict[digit_name]
                else:
                    if word.startswith(digit_name) or word.endswith(digit_name):
                        return digits_dict[digit_name]        
     
    first = find_digit()
    last = find_digit(reversed=True)
    result += int(str(first) + str(last))

print(result) # 56324