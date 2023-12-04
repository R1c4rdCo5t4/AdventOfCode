
def get_matches(line: str) -> int:
    winning, mine = [card.split(" ") for card in " ".join(line.split(" ")[2:]).split("|")]
    return len(set(filter(None, winning)).intersection(filter(None, mine)))