import csv

def load_interactions(csv_path: str) -> list[dict]:
    interactions = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            interactions.append({
                "drug_a": row["Drug_A"].strip().lower(),
                "drug_b": row["Drug_B"].strip().lower(),
                "level": row["Level"].strip(),
                "id_a": row["DDInterID_A"],
                "id_b": row["DDInterID_B"],
            })

    return interactions