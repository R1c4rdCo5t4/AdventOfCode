from rules import *

ordering, updates = parse_rules()
ordering_dict = build_ordering_dict(ordering)
result = 0
for update in updates:
    if is_valid(update, ordering_dict):
        result += int(update[len(update) // 2])

print(result) ## 6612
