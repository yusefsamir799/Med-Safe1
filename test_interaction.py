# Sample interaction data
interactions = [
    {"drug_a": "Aspirin", "drug_b": "Ibuprofen", "effect": "Increased bleeding risk"},
    {"drug_a": "Paracetamol", "drug_b": "Caffeine", "effect": "Enhanced effect"},
    {"drug_a": "Metformin", "drug_b": "Insulin", "effect": "Hypoglycemia risk"}
]

# Your case-insensitive index builder
def build_index(interactions):
    index = {}
    for interaction in interactions:
        key = frozenset([interaction["drug_a"].lower(), interaction["drug_b"].lower()])
        index[key] = interaction
    return index

# Function to look up an interaction
def find_interaction(index, drug1, drug2):
    key = frozenset([drug1.lower().strip(), drug2.lower().strip()])
    return index.get(key, None)

# Build the index
index = build_index(interactions)

# Test cases simulating real-world variations
test_cases = [
    ("aspirin", "ibuprofen"),
    ("Ibuprofen", "ASPIRIN"),
    ("  paracetamol", "CAFFEINE "),
    ("insulin", "metformin"),
    ("ParAcEtAmol", "cAffeine"),
    ("Metformin", "Insulin")
]

# Run tests
for d1, d2 in test_cases:
    result = find_interaction(index, d1, d2)
    print(f"{d1} + {d2} => {result}")
