def check_safety_combinations(original: list[int]):
    # tests combinations where each one removes one element
    for i in range(0, len(original)):
        report = original.copy()
        report.pop(i)
        if check_safety(report):
            return True

def check_safety(report: list[int]) -> bool:
    increasing = None
    
    for i in range(0, len(report) - 1):
        diff = report[i] - report[i+1]
        if diff == 0: # no diff
            break
        if increasing == None: # set direction
            increasing = diff > 0
        if increasing and diff < 0: # wrong direction
            break
        elif not increasing and diff > 0: # wrong direction
            break
        
        dist = abs(diff)
        if dist < 1 or dist > 3: # too far
            break
       
    else: # no breaks
        return True
    
    return False

with open("puzzle_input.txt") as f:
    reports = f.read().splitlines()
    safe_reports = 0

    for r in reports:
        report = [int(num) for num in r.split(" ")]
        if check_safety(report) or check_safety_combinations(report):
            safe_reports += 1

    print(safe_reports) # 404
