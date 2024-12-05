def parse_rules():
    """parses the rules from the input"""

    with open("puzzle_input.txt") as f:
        ordering, updates = [rule.split("\n") for rule in f.read().split("\n\n")]
        ordering = [s.split('|') for s in ordering]
        updates = [s.split(',') for s in updates]
    return ordering, updates

def build_ordering_dict(ordering: list) -> dict:
    """builds the dictionary with ordering rules"""

    ordering_dict = {}
    for before, after in ordering:
        if after not in ordering_dict:
            ordering_dict[after] = set()
        ordering_dict[after].add(before)
    return ordering_dict

def is_valid(update: list, ordering_dict: dict) -> bool:
    """checks if an update is valid according to the ordering rules"""
    
    for i, before in enumerate(update):
        for after in ordering_dict.get(before, set()):
            if after in update and update.index(after) > i:
                return False
    return True

def reorder_update(update: list, ordering_dict: dict) -> list:
    """reorders an update by sorting based on the ordering rules"""

    # custom comparison function
    def compare(a, b): 
        if b in ordering_dict.get(a, set()):
            return -1
        if a in ordering_dict.get(b, set()):
            return 1
        return 0

    return sorted(update, key=lambda a: [compare(a, b) for b in update])