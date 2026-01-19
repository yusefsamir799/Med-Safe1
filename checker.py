from itertools import combinations

def check_interactions(drugs: list[str], interaction_index: dict) -> list[dict]:
    found = []

    normalized = [d.strip().lower() for d in drugs]

    for d1, d2 in combinations(normalized, 2):
        key = frozenset([d1, d2])
        if key in interaction_index:
            found.append(interaction_index[key])

    return found