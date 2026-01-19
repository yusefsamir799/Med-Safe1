from checker import check_interactions

def test_known_interaction():
    index = {
        frozenset(["dexamethasone", "dolutegravir"]): {
            "drug_a": "dexamethasone",
            "drug_b": "dolutegravir",
            "level": "Minor"
        }
    }

    result = check_interactions(
        ["Dexamethasone", "Dolutegravir"],
        index
    )

    assert len(result) == 1
    assert result[0]["level"] == "Minor"


def test_no_interaction():
    index = {}
    result = check_interactions(["Aspirin", "Paracetamol"], index)
    assert result == []
