from loader import load_interactions


data = load_interactions("drug_interaction.csv")

def test_csv_loading():
    assert len(data) > 0
    assert "drug_a" in data[0]
    assert "drug_b" in data[0]
    assert "level" in data[0]


print(len(data))
