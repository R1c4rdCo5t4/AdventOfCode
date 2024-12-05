from rules import *

ordering, updates = parse_rules()
ordering_dict = build_ordering_dict(ordering)
result = 0
for update in updates:
    if not is_valid(update, ordering_dict):
        ordered_update = reorder_update(update, ordering_dict)
        result += int(ordered_update[len(ordered_update) // 2])

print(result) ## 4944
