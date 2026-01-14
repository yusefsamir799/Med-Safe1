import streamlit as st

from loader import load_interactions
from search import build_interaction_index
from checker import check_interactions


st.title("Drug Interaction Checker")

st.caption(
    "Enter two or more drug names separated by commas. "
    "The system checks known drug–drug interactions based on the loaded dataset."
)

# Load data
interactions = load_interactions("drug_interaction.csv")
interaction_index = build_interaction_index(interactions)

st.write("Enter drug names separated by commas:")

user_input = st.text_input(
    "Drugs",
    placeholder="Aspirin, Warfarin"
)

if st.button("Check interactions"):
    drugs = [d.strip() for d in user_input.split(",") if d.strip()]

    if len(drugs) < 2:
        st.warning("Please enter at least two drugs.")
    else:
        results = check_interactions(drugs, interaction_index)

        if results:
            st.error("⚠️ Potential interactions found:")
            for r in results:
                st.write(
                    f"- **{r['drug_a'].title()} + {r['drug_b'].title()}** "
                    f"(Severity: {r['level']})"
                )
        else:
            st.success("✅ No known interactions found.")
