from loader import load_interactions

def test_csv_loading():
    data = load_interactions("drug_interaction.csv")
    assert len(data) > 0
    assert "drug_a" in data[0]
    assert "drug_b" in data[0]
    assert "level" in data[0]
    
from loader import load_interactions

data = load_interactions(
    r"C:\Users\Bassem\OneDrive\Desktop\Youssef\drug_interaction.csv"
)

len(data)