from search import build_interaction_index

def test_build_interaction_index():
    interactions = [
        {
            "drug_a": "aspirin",
            "drug_b": "warfarin",
            "level": "High"
        }
    ]

    index = build_interaction_index(interactions)

    key = frozenset(["aspirin", "warfarin"])

    assert key in index
    assert index[key]["level"] == "High"
