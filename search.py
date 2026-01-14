def build_interaction_index(interactions):
    index = {}

    for interaction in interactions:
        key = frozenset([interaction["drug_a"], interaction["drug_b"]])
        index[key] = interaction

    return index
